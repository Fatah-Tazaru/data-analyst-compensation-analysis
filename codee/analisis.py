from pathlib import Path
import pandas as pd
from scipy.stats import kruskal
from itertools import combinations
from scipy.stats import mannwhitneyu

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent / "Filee" / "clean_data.csv"

df = pd.read_csv(file_path)

print("Shape: ", df.shape)

print("\nColumns: ")
print(df.columns.tolist())

print("\nInfo: ")
df.info()

print("\nHead: ")
print(df.head())


# ==========================================
# EXPERIENCE
# ==========================================

print("\n=== JUMLAH DATA ANALYST BERDASARKAN EXPERIENCE ===")

print(
    df["Experience"].value_counts()
)


# ==========================================
# RINGKASAN GAJI
# ==========================================

summary_salary = (
    df.groupby("Experience")["salary_in_usd"]
    .agg(["mean", "median", "count"])
    .reset_index()
)

print("\n=== RINGKASAN GAJI DATA ANALYST ===")
print(summary_salary)


# ==========================================
# STATISTIK DESKRIPTIF
# ==========================================

print("\n=== STATISTIK SALARY DATA ANALYST ===")

print(
    df["salary_in_usd"].describe()
)


# ==========================================
# GAJI TERTINGGI
# ==========================================

print("\n=== 20 GAJI TERTINGGI ===")

print(
    df[
        [
            "Designation",
            "Experience",
            "salary_in_usd"
        ]
    ]
    .sort_values(
        "salary_in_usd",
        ascending=False
    )
    .head(20)
)


# ==========================================
# MEAN DENGAN DAN TANPA NILAI EXTREME
# ==========================================

print("\n=== MEAN DENGAN DAN TANPA NILAI EXTREME ===")

mean_original = df["salary_in_usd"].mean()

print("Mean asli:")
print(mean_original)


df_no_extreme = df[
    df["salary_in_usd"] < 300000
]

print("\nMean salary < $300,000:")
print(
    df_no_extreme["salary_in_usd"].mean()
)


# ==========================================
# IQR OUTLIER
# ==========================================

Q1 = df["salary_in_usd"].quantile(0.25)

Q3 = df["salary_in_usd"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR


print("\n=== IQR OUTLIER ===")

print("Q1:", Q1)

print("Q3:", Q3)

print("IQR:", IQR)

print("Lower bound:", lower_bound)

print("Upper bound:", upper_bound)


# ==========================================
# MENCARI POTENTIAL OUTLIER
# ==========================================

outliers = df[
    (df["salary_in_usd"] < lower_bound)
    |
    (df["salary_in_usd"] > upper_bound)
]


print("\nJumlah potential outliers:")
print(len(outliers))


print("\nPotential outliers:")

print(
    outliers[
        [
            "Designation",
            "Experience",
            "salary_in_usd"
        ]
    ]
    .sort_values(
        "salary_in_usd",
        ascending=False
    )
    .to_string(index=False)
)

# ==========================================
# RATA RATA GAJI DENGAN EXPERIENCE
# ==========================================

print("\n=== Rata rata gaji berdasarkan Experience ===")

summary_salary = (
    df.groupby("Experience")
    ["salary_in_usd"]
    .agg(["mean", "median", "count"])
    .sort_values("mean",
    ascending=False)
  )
  
print(summary_salary)
  
# ==========================================
# EXPERIENCE DENGAN RATA RATA GAJI TERTINGGI
# ==========================================

print("\n=== EXPERIENCE DENGAN RATA RATA GAJI TERTINGGI ===")

result = (
    df.groupby("Experience")
    ["salary_in_usd"]
    .mean()
    .sort_values(ascending=False)
  )
  
print(result)

# ==========================================
# MEAN VS MEDIAN BERDASARKAN EXPERIENCE
# ==========================================

print("\n=== MEAN VS MEDIAN BERDASARKAN EXPERIENCE ===")

comparison = (
    df.groupby("Experience")
    ["salary_in_usd"]
    .agg(["mean", "median", "count"])
    .reset_index()
  )
  
comparison["difference"] = (
    comparison["mean"] - 
    comparison["median"]
  )
  
print(comparison)

# ==========================================
# RATA RATA GAJI BERDASARKAN DESIGNATION
# ==========================================

print("\n=== RATA RATA GAJI BERDASARKAN DESIGNATION ===")

summary_designation = (
    df.groupby("Designation")
    ["salary_in_usd"]
    .agg(["mean", "median", "count"])
    .sort_values("mean",
    ascending=False
      )
  )
  
print(summary_designation)

print("\n=== 10 DESIGNATION DENGAN RATA RATA GAJI TERTINGGI ===")

print(
    summary_designation
    .head(10)
  )
  
# ==========================================
# RATA RATA GAJI BERDASARKAN COMPANY SIZE
# ==========================================

print("\n===  RATA RATA GAJI BERDASARKAN COMPANY SIZE ===")

summary_company = (
    df.groupby("Company_Size")
    ["salary_in_usd"]
    .agg(["mean", "median", "count"])
    .sort_values("mean",
    ascending=False
      )
  )
  
print(summary_company)
  
print("\n=== COMPANY SIZE BERDASARKAN GAJI TERTINGGI ===")

print(
    summary_company["mean"]
    .sort_values(ascending=False)
  )
  
# ==========================================
# RATA RATA GAJI BERDASARKAN REMOTE WORKING
# ==========================================

print("\n=== RATA RATA GAJI BERDASARKAN REMOTE WORKING ===")

summary_remote = (
    df.groupby("Remote_Working_Ratio")
    ["salary_in_usd"]
    .agg(["mean", "median", "count"])
    .sort_values("mean",
      ascending=False
    )
  )
  
print(summary_remote)

print("\n=== REMOTE WORKING DENGAN RATA RATA GAJI TERTINGGI ===")

print(
    summary_remote["mean"]
    .sort_values(
      ascending=False
    )
  )
  
# ==========================================
# RATA RATA GAJI : EXPERIENCE X COMPANY SIZE
# ==========================================

print("\n=== RATA RATA GAJI : EXPERIENCE X COMPANY SIZE ===")

experience_company = (
    df.pivot_table(
      values="salary_in_usd",
      index="Experience",
      columns="Company_Size",
      aggfunc="mean"
      )
  )
  
print(experience_company)

# ==========================================
# JUMLAH DATA : EXPERIENCE X COMPANY SIZE
# ==========================================


print("\n=== JUMLAH DATA : EXPERIENCE X COMPANY SIZE ===")

count_experience_company = (
    df.pivot_table(
      values="salary_in_usd",
      index="Experience",
      columns="Company_Size",
      aggfunc="count"
      )
  )
  
print(count_experience_company)

# ==========================================
# RATA RATA GAJI BERDASARKAN COMPANY LOCATION
# ==========================================

print("\n=== RATA RATA GAJI BERDASARKAN COMPANY LOCATION ===")

summary_location = (
    df.groupby("Company_Location")
    ["salary_in_usd"]
    .agg(["mean", "median", "count"])
    .sort_values("mean",
      ascending=False
      )
  )
  
print(summary_location)

print("\n=== 10 COMPANY LOCATION DENGAN RATA RATA GAJI TERTINGGI ===")

print(
  summary_location.head(10)
  )
  
# ==========================================
# RATA RATA GAJI : EXPERIENCE X REMOTE WORKING
# ==========================================

print("\n=== RATA RATA GAJI : EXPERIENCE X REMOTE WORKING ===")

experience_remote = (
    df.pivot_table(
        values="salary_in_usd",
        index="Experience",
        columns="Remote_Working_Ratio",
        aggfunc="mean"
    )
    .reindex(["EN", "MI", "SE", "EX"])
)

print(experience_remote)

print("\n=== JUMLAH DATA : EXPERIENCE X REMOTE WORKING ===")

experience_remote_count = (
    df.pivot_table(
        values="salary_in_usd",
        index="Experience",
        columns="Remote_Working_Ratio",
        aggfunc="count"
    )
    .reindex(["EN", "MI", "SE", "EX"])
)

print(experience_remote_count)

# ==========================================
# SAMPLE PROPORTION ANALYSIS
# ==========================================

print("\n=== PROPORSI EXPERIENCE ===")

experience_count = df["Experience"].value_counts()
experience_pct = (
    df["Experience"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

experience_summary = pd.DataFrame({
    "count": experience_count,
    "percentage": experience_pct
})

print(experience_summary)


print("\n=== PROPORSI COMPANY SIZE ===")

company_size_count = df["Company_Size"].value_counts()
company_size_pct = (
    df["Company_Size"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

company_size_summary = pd.DataFrame({
    "count": company_size_count,
    "percentage": company_size_pct
})

print(company_size_summary)


print("\n=== PROPORSI REMOTE WORKING ===")

remote_count = df["Remote_Working_Ratio"].value_counts()
remote_pct = (
    df["Remote_Working_Ratio"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

remote_summary = pd.DataFrame({
    "count": remote_count,
    "percentage": remote_pct
})

print(remote_summary)


# ==========================================
# STATISTICAL TEST
# ==========================================


print("\n=== KRUSKAL-WALLIS TEST: EXPERIENCE VS SALARY ===")

groups = [
    group["salary_in_usd"].values
    for _, group in df.groupby("Experience")
]

kw_statistic, kw_p_value = kruskal(*groups)

n = len(df)
k = len(groups)

epsilon_squared = (
    kw_statistic - k + 1
) / (
    n - k
)

print("H-statistic:", kw_statistic)
print("p-value:", kw_p_value)
print("Epsilon-squared:", epsilon_squared)

if kw_p_value < 0.05:
    print("Result: Significant difference between experience groups.")
else:
    print("Result: No statistically significant difference between experience groups.")
    
# ==========================================
# POST-HOC MANN-WHITNEY U TEST
# WITH HOLM CORRECTION
# ==========================================


print("\n=== POST-HOC MANN-WHITNEY U TEST ===")

experience_groups = {
    experience: group["salary_in_usd"].values
    for experience, group in df.groupby("Experience")
}

results = []

for group1, group2 in combinations(experience_groups.keys(), 2):

  u_statistic, mw_p_value = mannwhitneyu(
        experience_groups[group1],
        experience_groups[group2],
        alternative="two-sided"
    )

  results.append({
        "Group 1": group1,
        "Group 2": group2,
        "U statistic": u_statistic,
        "raw p-value": mw_p_value
    })


posthoc_df = pd.DataFrame(results)


# ==========================================
# HOLM CORRECTION
# ==========================================

sorted_indices = (
    posthoc_df["raw p-value"]
    .argsort()
    .tolist()
)

m = len(posthoc_df)

adjusted_p = [0.0] * m

for rank, index in enumerate(sorted_indices):
    adjusted_p[index] = min(
        1.0,
        posthoc_df.loc[index, "raw p-value"] * (m - rank)
    )

# Pastikan adjusted p-value bersifat monoton
for i in range(1, len(sorted_indices)):
    previous_index = sorted_indices[i - 1]
    current_index = sorted_indices[i]

    adjusted_p[current_index] = max(
        adjusted_p[previous_index],
        adjusted_p[current_index]
    )

posthoc_df["adjusted p-value"] = adjusted_p

posthoc_df["significant"] = (
    posthoc_df["adjusted p-value"] < 0.05
)

print(posthoc_df)
