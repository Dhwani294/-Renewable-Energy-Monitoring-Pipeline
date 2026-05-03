import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = "energy-readings"

site_ids = [f"site_{i}" for i in range(1, 11)]
site_types = {sid: random.choice(["solar", "wind"]) for sid in site_ids}

def generate_reading(site_id):
    site_type = site_types[site_id]

    # Simulate realistic values
    energy = round(random.uniform(50, 500), 2)
    temp = round(random.uniform(15, 40), 2)
    wind = round(random.uniform(2, 15), 2)
    efficiency = round(random.uniform(60, 95), 2)

    # Introduce occasional corrupt/null values
    if random.random() < 0.05:
        energy = None

    return {
        "site_id": site_id,
        "site_type": site_type,
        "timestamp": datetime.utcnow().isoformat(),
        "energy_output_kwh": energy,
        "temperature_c": temp,
        "wind_speed_mps": wind,
        "panel_efficiency_pct": efficiency
    }

if __name__ == "__main__":
    while True:
        for site in site_ids:
            data = generate_reading(site)
            producer.send(TOPIC, value=data)
            print(f"Sent: {data}")
        time.sleep(5)
