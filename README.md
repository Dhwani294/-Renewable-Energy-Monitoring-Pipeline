# ⚡ Real-Time Renewable Energy Monitoring Pipeline

A production-style **end-to-end data engineering project** that simulates, processes, and analyzes real-time renewable energy data using modern big data tools.

---

## 🌍 Project Overview

This project replicates a real-world **IoT-based renewable energy monitoring system**, where solar and wind energy sites continuously generate data. The pipeline ingests, processes, and analyzes this data in real-time to enable **operational insights and anomaly detection**.

---

## 🏗️ Architecture

```
IoT Sensor Simulator (Python)
            ↓
      Apache Kafka
            ↓
 PySpark Structured Streaming
            ↓
      Delta Lake (Data Lake)
            ↓
        Spark SQL
            ↓
        Power BI Dashboard
```

---

## 🚀 Key Features

✨ **Real-Time Data Streaming**

* Simulates IoT sensor data from multiple renewable energy sites
* Streams data continuously via Kafka

📊 **Advanced Data Processing**

* Cleans and transforms streaming data using PySpark
* Handles nulls, corrupt records, and schema enforcement

⚡ **Anomaly Detection**

* Detects sudden drops (>30%) in energy output
* Uses rolling window aggregations for real-time monitoring

🧱 **Medallion Architecture (Industry Standard)**

* **Bronze** → Raw ingestion
* **Silver** → Cleaned + structured data
* **Gold** → Aggregated insights

📁 **Efficient Data Storage**

* Uses Delta Lake for:

  * ACID transactions
  * Time travel
  * Scalable storage

📈 **Business Insights Ready**

* Pre-built SQL queries for analytics
* Power BI-ready dataset for visualization

---

## 📂 Project Structure

```
├── producer/        # Kafka producer (IoT simulator)
├── consumer/        # PySpark streaming pipeline
├── sql/             # Analytical SQL queries
├── notebooks/       # Databricks / exploration notebooks
├── dashboard/       # Power BI files (optional)
├── configs/         # Configuration files
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Start Kafka (Docker)

```bash
docker-compose up -d
```

---

### 2️⃣ Run Kafka Producer

```bash
python producer/producer.py
```

---

### 3️⃣ Run Streaming Consumer

```bash
spark-submit consumer/consumer.py
```

---

### 4️⃣ Query Data (Optional)

Use Spark SQL or notebooks to run queries from `/sql` folder.

---

## 📊 Sample Analytics Use Cases

* 📅 **Daily Energy Yield per Site**
* 📈 **Month-over-Month Generation Trends**
* ⚠️ **Top Underperforming Sites**
* ⚙️ **Capacity Utilization**
* 📉 **7-Day Rolling Average Comparison**

---

## 🧰 Tech Stack

| Layer           | Technology                   |
| --------------- | ---------------------------- |
| Data Simulation | Python                       |
| Streaming       | Apache Kafka                 |
| Processing      | PySpark Structured Streaming |
| Storage         | Delta Lake                   |
| Query Engine    | Spark SQL                    |
| Visualization   | Power BI                     |
| Orchestration   | Docker                       |

---

## 💡 Why This Project Matters

This project demonstrates **real-world data engineering skills**:

* Designing scalable streaming pipelines
* Working with distributed systems (Kafka + Spark)
* Implementing data quality and anomaly detection
* Using modern data lake architecture

---

## 🔮 Future Improvements

* 🔁 Add Airflow for orchestration
* ☁️ Deploy on Azure (Data Lake Gen2 + Databricks)
* 📡 Integrate real IoT APIs
* 📊 Build interactive Power BI dashboards
* 🧪 Add unit + integration testing

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork, improve, and submit a PR.

---

## ⭐ Final Note

This project is designed to showcase **job-ready data engineering skills** and demonstrate how real-time data pipelines power modern renewable energy systems.

---

🚀 *Built to learn. Designed to impress.*
