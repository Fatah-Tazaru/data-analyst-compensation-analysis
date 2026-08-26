from pathlib import Path
import pandas as pd

# =========================
# 1. LOAD DATA
# =========================

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent/ "Filee" / "DataScience_Salaries_And_Fields.csv"
df = pd.read_csv(file_path)

# =========================
# 2. STRUKTUR DATA
# =========================

print("\n=== STRUKTUR DATA ===")

print("Shape: ", df.shape)

print("\nColumns: ")
print(df.columns.tolist())

print("\nHead: ")
print(df.head())

print("\nTail: ")
print(df.tail())

print("\nInfo: ")
print(df.info())

# =========================
# 3. PROFILLING SETIAP KOLOM
# =========================

print("\n=== PROFILLING KOLOM ===")

for col in df.columns:
  print("\n", "=" * 50)
  print(col)
  
  print("Contoh nilai: ")
  print(df[col].head())
  
  print("Jumlah unique: ", df[col].nunique())
  print("Jumlah Missing: ", df[col].isna().sum())
  
# =========================
# 4. DUPLIKAT
# =========================

print("\n=== DUPLIKAT ===")

print("Jumlah duplikat: ", df.duplicated().sum())

print(
  "Jumlah seluruh baris dalam kelompok duplikat: ",
  df.duplicated(keep=False).sum()
  )
  
# =========================
# 5. INVESTIGASI Unnamed: 0
# =========================

print("\n === INVESTIGASI Unnamed: 0")

print("Nilai awal:")
print(
  df["Unnamed: 0"].dropna().head(20)
  )

print("\nNilai akhir: ")
print(
  df["Unnamed: 0"].dropna().tail(20)
  )
  
print(
  "Jumlah nilai: ",
  df["Unnamed: 0"].notna().sum()
  )
  
print(
  "Jumlah unique: ",
  df["Unnamed: 0"].nunique()
  )

# =========================
# 6. INVESTIGASI MISSING SALARY
# =========================

print("\n=== INVESTIGASI MISSING SALARY ===")

Missing_salary = (
  df["Salary_Currency"].isna()
  &
  df["salary_in_usd"].isna()
  )
  
print("Salary_Currency dan salary_in_usd kosong bersamaan: ", Missing_salary.sum())

# =========================
# 7. PERBANDINGAN DUA KOLOM USD
# =========================

print("\n=== PERBANDINGAN SALARY USD ===")

different_salary = df[
  df["salary_in_usd"].notna()
  &
  df["Salary_In_USD"].notna()
  &
  (
    df["salary_in_usd"]
    !=
    df["Salary_In_USD"]
    )
  ]
  
print(
  "Jumlah nilai berbeda: ",
  len(different_salary)
  )
  
print(
  different_salary[
    [
      "Salary_In_Rupees",
      "Salary_Currency",
      "salary_in_usd",
      "Salary_In_USD"
      ]
    ].head(20)
  )
  
# =========================
# 8.MELIHAT POLA Salary_In_USD
# =========================

print("\n=== CONTOH Salary USD ===")

print(
  df[
    df["salary_in_usd"].notna()
    ][
      [
        "Salary_In_Rupees",
        "Salary_Currency",
        "salary_in_usd",
        "Salary_In_USD"
        ]
      ].head(20)
  )
  
# =========================
# 9. MELIHAT CONTOH DUPLIKAT
# =========================

print("\n=== CONTOH DUPLIKAT ===")

duplikat = df[
  df.duplicated(keep=False)
  ]
  
print(
  duplikat.head(20).to_string()
  )