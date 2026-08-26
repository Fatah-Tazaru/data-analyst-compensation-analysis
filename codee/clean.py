from pathlib import Path
import pandas as pd

# =========================
# 1. LOAD DATA
# =========================

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent/ "Filee" / "DataScience_Salaries_And_Fields.csv"
df = pd.read_csv(file_path)

print("=== DATA CLEANING ===")
print("Data awal: ", df.shape)

# =========================
# 2. HAPUS KOLOM TIDAK RELEVAN
# =========================

df = df.drop(columns=["Unnamed: 0"])

print(
  "Setelah Unnamed: 0 dihapus: ", df.shape
  )
  
# =========================
# 3. HAPUS DUPLIKAT
# =========================

df = df.drop_duplicates()

print(
  "Setelah duplicate dihapus: ", df.shape
  )
  
# =========================
# 4. BUAT DATA ANALISIS YANG MEMILIKI USD
# =========================


analysis_data = df.dropna(
  subset=["salary_in_usd"]
  )
  
print(
  "Setelah menangani missing salary usd: ",
  analysis_data.shape
  )
  
# =========================
# 5. FILTER DATA ANALISIS
# =========================

da_data = analysis_data[
  analysis_data["Designation"].str.contains(
    "Data analyst",
    case=False,
    na=False
    )
  ]
  
print(
  "Jumlah Data analyst: ",
  len(da_data)
  )
  
# =========================
# 6. SIMPAN DATA HASIL CLEANING
# =========================

output_path = (
  BASE_DIR.parent /"Filee" / "clean_data.csv"
  )
  
da_data.to_csv(
  output_path,
  index=False
  )
  
print(
  "File cleaned berhasil disimpan: "
  )
print(output_path)