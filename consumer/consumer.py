from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder     .appName("EnergyStreaming")     .getOrCreate()

schema = StructType([
    StructField("site_id", StringType()),
    StructField("site_type", StringType()),
    StructField("timestamp", StringType()),
    StructField("energy_output_kwh", DoubleType()),
    StructField("temperature_c", DoubleType()),
    StructField("wind_speed_mps", DoubleType()),
    StructField("panel_efficiency_pct", DoubleType())
])

df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "energy-readings")     .load()

json_df = df.selectExpr("CAST(value AS STRING)")     .select(from_json(col("value"), schema).alias("data"))     .select("data.*")

clean_df = json_df.dropna(subset=["energy_output_kwh"])

clean_df = clean_df.withColumn("timestamp", to_timestamp("timestamp"))

windowed = clean_df     .withWatermark("timestamp", "10 minutes")     .groupBy(
        window("timestamp", "5 minutes"),
        "site_id"
    ).agg(avg("energy_output_kwh").alias("rolling_avg"))

joined = clean_df.join(windowed, "site_id")

final_df = joined.withColumn(
    "anomaly_flag",
    when(col("energy_output_kwh") < 0.7 * col("rolling_avg"), 1).otherwise(0)
)

query = final_df.writeStream     .format("delta")     .option("checkpointLocation", "/tmp/checkpoints")     .start("/tmp/delta-energy")

query.awaitTermination()
