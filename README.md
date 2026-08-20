E-Commerce ETL Data Pipeline \& Analytics Dashboard



Project End-to-End Data Engineering untuk menarik data e-commerce dari REST API, mengolahnya menggunakan Python \& Pandas, menyimpan data ke Cloud Database PostgreSQL (Supabase), dan memvisualisasikannya di Looker Studio.



 Tech Stack & Tools

Language: Python 3.12

Data Transformation: Pandas

Database Connection:SQLAlchemy \& Psycopg2

Database Cloud: Supabase (PostgreSQL)

Visualization: Google Looker Studio

Data Source: DummyJSON REST API



 Pipeline Architecture

1. Extract:   Fetch 100 data produk dari API `https://dummyjson.com/products`.

2. Transform: Pembersihan data, restrukturisasi kolom, dan penambahan timestamp menggunakan `pandas`.

3. Load: Unggah data otomatis ke tabel `store\_sales\_data` di Supabase.

4. Visualize: Koneksi langsung dari Supabase ke Looker Studio untuk pemantauan KPI bisnis (Total Produk, Stok, Rata-rata Harga \& Rating).



Dashboard




 Cara Menjalankan Script

1. Clone repository ini:

&#x20;  ```bash

&#x20;  git clone <URL\_REPOSITORY\_GITHUB\_ANDA>

&#x20;  cd ecommerce

