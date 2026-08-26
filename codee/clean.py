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

before_duplicate = len(df)

df = df.drop_duplicates()

after_duplicate = len(df)
removed_duplicate = before_duplicate - after_duplicate

print("Setelah duplicate dihapus: ", df.shape)
print("Duplicate rows dihapus: ", removed_duplicate)
  
# =========================
# 4. BUAT DATA ANALISIS YANG MEMILIKI USD
# =========================

before_missing = len(df)

analysis_data = df.dropna(
    subset=["salary_in_usd"]
)

after_missing = len(analysis_data)
removed_missing = before_missing - after_missing

print("Setelah menangani missing salary usd: ", analysis_data.shape)
print("Missing salary rows dihapus: ", removed_missing)
  
# =========================
# 5. FILTER DATA ANALISIS
# =========================

before_filter = len(analysis_data)

da_data = analysis_data[
    analysis_data["Designation"].str.contains(
        "Data analyst",
        case=False,
        na=False
    )
]

after_filter = len(da_data)
removed_filter = before_filter - after_filter

print("Jumlah Data analyst: ", len(da_data))
print("Rows di luar Data Analyst: ", removed_filter)
  
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