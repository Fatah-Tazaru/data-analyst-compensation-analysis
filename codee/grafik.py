from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. BACA DATA
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent / "Filee" / "clean_data.csv"
df = pd.read_csv(file_path)

# ==========================================
# 2. BUAT FOLDER OUTPUT
# ==========================================

output_dir = BASE_DIR.parent/ "outputs" / "charts"
output_dir.mkdir(
    parents=True,
    exist_ok=True
  )
  
  # ==========================================
# 3. GRAFIK DISTRIBUSI SALARY
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["salary_in_usd"],
    bins=30,
    kde=True
  )
  
plt.title("Distribusi Salary Data Analyst")

plt.xlabel("Salary (USD)")

plt.ylabel("Jumlah Data")

plt.tight_layout()

plt.savefig(
    output_dir /
    "salary_distribution.png"
  )
  
plt.close()

# ==========================================
# 4. RATA RATA GAJI BERDASARKAN EXPERIENCE
# ==========================================

summary_salary = (
    df.groupby(
      "Experience")["salary_in_usd"]
      .mean()
      .reindex(["EN", "MI", "SE", "EX" ])
  )
  
plt.figure(figsize=(8, 6))

sns.barplot(
    x=summary_salary.index,
    y=summary_salary.values
  )
  
plt.title("Rata rata Salary Berdasarkan Experience")

plt.xlabel("Experience")

plt.ylabel("Average Salary (USD)")

plt.tight_layout()

plt.savefig(
    output_dir /
    "average_salary_by_experience.png"
  )
  
plt.close()
  
# ==========================================
# 5. JUMLAH DATA BERDASARKAN EXPERIENCE
# ==========================================

Experience_count = (
    df["Experience"]
    .value_counts()
    .reindex(["EN", "MI", "SE", "EX"])
  )
  
plt.figure(figsize=(8, 6))

sns.barplot(
    x=Experience_count.index,
    y=Experience_count.values
  )
  
plt.title(
  "Jumlah Data Berdasarkan Experience"
  )

plt.xlabel("Experience")

plt.ylabel("Jumlah data")

plt.tight_layout()

plt.savefig(
    output_dir /
    "count_by_experience.png"
  )
  
plt.close()

# ==========================================
# 6. BOXPLOT SALARY BERDASARKAN EXPERIENCE
# ==========================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Experience",
    y="salary_in_usd",
    order=["EN", "MI", "SE", "EX"]
  )

plt.title("Distribusi Salary Berdasarkan Experience")

plt.xlabel("Experience")

plt.ylabel("Salary (USD)")

plt.tight_layout()

plt.savefig(
    output_dir /
    "salary_boxplot_by_experience.png"
  )
  
plt.close()

# ==========================================
# SALARY EXPERIENCE COMPANY HEATMAP
# ==========================================

experience_company = (
    df.pivot_table(
      values="salary_in_usd",
      index="Experience",
      columns="Company_Size",
      aggfunc="mean"
      )
  )
  
plt.figure(figsize=(8, 5))

sns.heatmap(
    experience_company,
    annot=True,
    fmt=".0f"
  )
  
plt.title("Rata rata Salary Berdasarkan Experience dan Company Size")
plt.xlabel("Company Size")
plt.ylabel("Experience")

plt.tight_layout()

plt.savefig(
    output_dir /
    "salary_experience_company_heatmap.png"
  )

# ==========================================
# 7. COMPANY LOCATION - JUMLAH DATA TERBANYAK
# ==========================================

location_count = (
    df["Company_Location"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=location_count.values,
    y=location_count.index
)

plt.title("10 Company Location dengan Jumlah Data Terbanyak")
plt.xlabel("Jumlah Data")
plt.ylabel("Company Location")

plt.tight_layout()

plt.savefig(
    output_dir /
    "top_company_location_count.png"
)

plt.close()

plt.close()

# ==========================================
# 8. SALARY EXPERIENCE X REMOTE WORKING
# ==========================================

experience_remote = (
    df.pivot_table(
        values="salary_in_usd",
        index="Experience",
        columns="Remote_Working_Ratio",
        aggfunc="mean"
    )
    .reindex(["EN", "MI", "SE", "EX"])
)

plt.figure(figsize=(8, 5))

sns.heatmap(
    experience_remote,
    annot=True,
    fmt=".0f"
)

plt.title(
    "Rata rata Salary Berdasarkan Experience dan Remote Working"
)

plt.xlabel("Remote Working Ratio (%)")
plt.ylabel("Experience")

plt.tight_layout()

plt.savefig(
    output_dir /
    "salary_experience_remote_heatmap.png"
)

plt.close()

print("\n=== GRAFIK SELESAI ===")

print("Folder Output: ")
print(output_dir)

print("\nFile grafik: ")

print("1.salary_distribution.png")
print("2. average_salary_by_experience.png")
print("3. count_by_experience.png")
print("4. salary_boxplot_by_experience.png")
print("5. salary_experience_company_heatmap.png")
print("6. top_company_location_count.png")
print("7. salary_experience_remote_heatmap.png")