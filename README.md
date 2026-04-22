### 🚨 Big Data Technology 2026 – Real-Time Fraud Detection System

## 🔐 Keamanan dan Privasi Big Data

**Studi Kasus: Real-Time Fraud Detection (Kafka + Spark + Streamlit)**

---

## 👨‍🏫 Dosen Pembimbing

[![GitHub - Muhayat Lab](https://img.shields.io/badge/GitHub-Muhayat--Lab-181717?logo=github\&style=for-the-badge)](https://github.com/muhayat-lab)

## 👨‍💻 Developer

[![GitHub - Zharvian](https://img.shields.io/badge/GitHub-Zharvians-007ACC?logo=github\&style=for-the-badge)](https://github.com/Zharvians)

**Nama:** Muhammad Ade Ramadhani
**NPM:** 230104040213
**Kelas:** TI23A

---

## 🧠 Deskripsi Proyek

Proyek ini merupakan implementasi **pipeline Big Data real-time** untuk mendeteksi aktivitas fraud (penipuan) pada transaksi perbankan.

Sistem ini menggabungkan:

* **Apache Kafka** → Streaming data transaksi
* **Apache Spark (Structured Streaming)** → Pemrosesan real-time
* **Streamlit** → Dashboard monitoring

📌 Fokus utama:

* Deteksi fraud secara real-time (low latency)
* Keamanan data (masking & encryption)
* Visualisasi data secara langsung

---

## 🏗 Arsitektur Sistem

```text
Kafka → Spark Streaming → Secure Processing → Storage → Dashboard
```

Penjelasan:

* Kafka: Mengirim data transaksi secara terus-menerus
* Spark: Memproses & mendeteksi fraud
* Storage: Menyimpan hasil streaming
* Dashboard: Menampilkan insight real-time

📖 Berdasarkan modul praktikum, pipeline ini mencerminkan sistem industri dengan kebutuhan:

* High throughput (ribuan transaksi/detik)
* Low latency
* Secure & scalable 

---

## ✨ Fitur Utama

* 🔄 Real-Time Data Streaming
* 🚨 Fraud Detection (Rule-Based)
* 🔐 Data Masking (rekening disamarkan)
* 🔒 Data Encryption (Base64 encoding)
* 📊 Dashboard Monitoring
* 📝 Logging aktivitas sistem
* ⚡ Micro-batch processing (Spark)

---

## 🛠 Teknologi yang Digunakan

```bash
• Python
• Apache Kafka
• Apache Spark (PySpark)
• Streamlit
• Pandas
• Parquet Storage
• Linux Environment
```

---

## 📂 Struktur Project

```bash
Kafka/
│
├── scripts/
│   ├── kafka_producer_bank.py
│   └── spark_streaming_fraud_v2.py
│
├── dashboard/
│   └── fraud_dashboard_v2.py
│
├── stream_data/
│   └── realtime_output/
│
├── logs/
│   └── fraud_realtime.log
│
└── README.md
```

---

## 🔐 Implementasi Keamanan

Berdasarkan modul praktikum:

### 1. Data Masking

```python
concat(lit("****"), col("rekening").substr(-2,2))
```

### 2. Encryption

```python
base64(col("jumlah").cast("string"))
```

### 3. Logging

* Aktivitas sistem dicatat untuk audit

📌 Insight penting:

> Data sensitif wajib diamankan melalui masking dan enkripsi 

---

## 🚨 Logic Fraud Detection

Rule sederhana:

```python
if jumlah > 50.000.000 → FRAUD
if lokasi == "Luar Negeri" → FRAUD
else → NORMAL
```

📌 Ini masih **rule-based detection**, sesuai modul:

* Rule-based → tahap awal
* AI-based → pengembangan selanjutnya 

---

## 🚀 Cara Menjalankan

### 1. Jalankan Kafka

```bash
# Terminal 1
bin/zookeeper-server-start.sh config/zookeeper.properties

# Terminal 2
bin/kafka-server-start.sh config/server.properties
```

### 2. Jalankan Producer

```bash
python scripts/kafka_producer_bank.py
```

### 3. Jalankan Spark Streaming

```bash
spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
scripts/spark_streaming_fraud_v2.py
```

### 4. Jalankan Dashboard

```bash
streamlit run dashboard/fraud_dashboard_v2.py
```

---

## 📊 Output Sistem

* Data transaksi real-time
* Status fraud / normal
* Dashboard interaktif
* File output (Parquet)

---

## 📜 Lisensi

```bash
Proyek ini dibuat untuk keperluan akademik
Big Data Technology 2026

Dilarang digunakan untuk kepentingan komersial.
© 2026 — Muhammad Ade Ramadhani
```

---
