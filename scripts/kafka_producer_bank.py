from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    jumlah = random.randint(100000,100000000)

    data = {
        "nama": random.choice(["Zharvian","Sora","Grace","Ahn","Olip"]),
        "rekening": str(random.randint(100000,999999)),
        "jumlah": jumlah,
        "lokasi": random.choice(["Jakarta", "Jepang", "Banjarmasin", "Balikpapan", "Depok", "Amerika", "China", "Prancis"]),
        "status": "FRAUD" if jumlah > 50000000 else "AMAN"  # 🔥 FIX
    }

    producer.send("bank_topic", value=data)
    print(data)
    time.sleep(2)