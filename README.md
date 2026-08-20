# 🛒 E-Commerce ETL Data Pipeline & Analytics Dashboard

![ETL Pipeline Status](https://github.com/Braviambat02181999/ETL-Pipeline-Project/actions/workflows/etl_schedule.yml/badge.svg)

Proyek *End-to-End Data Engineering* untuk menarik data e-commerce dari REST API, mengolahnya menggunakan Python & Pandas, menyimpannya secara otomatis ke Cloud Database PostgreSQL (Supabase) via GitHub Actions, serta memvisualisasikannya secara interaktif di Google Looker Studio.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.12
* **Data Transformation:** Pandas
* **Database Connection:** SQLAlchemy & Psycopg2
* **Cloud Database:** Supabase (PostgreSQL)
* **Automation / CI-CD:** GitHub Actions
* **Visualization:** Google Looker Studio
* **Data Source:** DummyJSON REST API

---

## 🏗️ Pipeline Architecture

1. **Extract:** Fetch 100 data produk dari REST API (`https://dummyjson.com/products`).
2. **Transform:** Pembersihan data, seleksi & restrukturisasi kolom, serta penambahan *timestamp* penarikan data menggunakan Pandas.
3. **Load:** Pengunggahan data otomatis ke tabel `store_sales_data` di Supabase PostgreSQL.
4. **Automation:** Eksekusi otomatis terjadwal menggunakan GitHub Actions (*Cron Schedule*).
5. **Visualize:** Koneksi live dari Supabase ke Looker Studio untuk memantau KPI bisnis (*Total Produk, Stok, Rata-rata Harga & Rating*).

---

## 🔗 Link Akses

* 💻 **GitHub Repository:** [https://github.com/Braviambat02181999/ETL-Pipeline-Project](https://github.com/Braviambat02181999/ETL-Pipeline-Project)
* 📊 **Interactive Dashboard:** [Google Looker Studio Dashboard](https://datastudio.google.com/reporting/2f789424-04a6-48be-8a06-8d43d5e1e3ba)

---

## 🚀 Cara Menjalankan Script Secara Lokal

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/Braviambat02181999/ETL-Pipeline-Project.git](https://github.com/Braviambat02181999/ETL-Pipeline-Project.git)
   cd ETL-Pipeline-Project
