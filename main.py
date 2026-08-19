import os
import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# 1. EXTRACT: Ambil data dari API
def fetch_store_data():
    url = "https://dummyjson.com/products?limit=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['products']
    else:
        raise Exception(f"Gagal mengambil data dari API: {response.status_code}")

# 2. TRANSFORM & LOAD: Olah data dengan Pandas & kirim ke Supabase
def process_and_load(raw_products):
    DB_URL = os.getenv('DATABASE_URL')
    if not DB_URL:
        raise ValueError("DATABASE_URL belum diatur!")

    # Mengubah JSON ke Pandas DataFrame
    df = pd.DataFrame(raw_products)
    
    # Pilih dan rename kolom sesuai tabel Supabase
    df = df[['title', 'category', 'price', 'discountPercentage', 'stock', 'rating']]
    df.columns = ['product_title', 'category', 'price_usd', 'discount_percentage', 'stock_qty', 'rating']
    
    # Tambah timestamp
    df['fetched_at'] = datetime.now()

    # Engine koneksi ke Supabase via psycopg2
    engine = create_engine(DB_URL)
    
    # Upload langsung ke tabel
    df.to_sql('store_sales_data', engine, if_exists='append', index=False)
    print(f"[{datetime.now()}] MANTAP! {len(df)} Data Berhasil Dimasukkan ke Supabase.")

if __name__ == "__main__":
    print("Memulai ETL E-Commerce Pipeline...")
    raw = fetch_store_data()
    process_and_load(raw)