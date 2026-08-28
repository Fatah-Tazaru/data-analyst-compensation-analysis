# 📊 Data Analyst Compensation Analysis

## 📌 Project Overview

This project analyzes salary patterns among **Data Analyst professionals** using a public dataset.

The analysis focuses on understanding how salary varies across:

- Experience level
- Job designation
- Company size
- Remote working ratio
- Company location
- Salary distribution
- Potential outliers

The project also applies statistical hypothesis testing to evaluate whether salary distributions differ significantly across experience levels.

The complete workflow covers:

**Data Intake → Data Cleaning → Exploratory Data Analysis → Outlier Analysis → Statistical Analysis → Visualization → Key Findings**

---

## 🎯 Objectives

The main objectives of this project are:

1. Understand the distribution of Data Analyst salaries.
2. Analyze salary differences across experience levels.
3. Compare salaries across different job designations.
4. Analyze salary differences based on company size.
5. Explore the relationship between remote working and salary.
6. Identify potential salary outliers.
7. Analyze sample proportions across important categorical variables.
8. Statistically test whether salary distributions differ across experience levels.
9. Present the findings through clear visualizations.

---

## Key Results

| Metric | Result |
|---|---:|
| Original Dataset | 15,445 rows |
| Cleaned Dataset | 9,127 rows |
| Data Analyst Records | 1,322 rows |
| Average Salary | ~$106.1K |
| Median Salary | ~$100K |
| Q1 Salary | ~$70K |
| Q3 Salary | ~$133K |
| Maximum Salary | ~$774K |

The analysis focuses on Data Analyst roles after removing duplicates and records with missing salary values.

---

## 📂 Dataset

The project uses the **Data Science Salaries And Fields** dataset.

The original dataset contains salary and employment information such as:

- Working Year
- Designation
- Experience
- Employment Status
- Salary
- Employee Location
- Company Location
- Company Size
- Remote Working Ratio
- Salary Currency
- Salary in USD

The analysis focuses specifically on records related to **Data Analyst** positions.

---

# 🧹 Data Cleaning

The original dataset contains **15,445 rows** and **13 columns**.

The following cleaning steps were performed:

1. Remove the unnecessary `Unnamed: 0` column.
2. Remove duplicate rows.
3. Remove records with missing `salary_in_usd`.
4. Filter the dataset to Data Analyst-related positions.

### Data Quality Summary

| Cleaning Step | Rows | Rows Removed |
|---|---:|---:|
| Raw dataset | 15,445 | - |
| Remove `Unnamed: 0` column | 15,445 | 0 |
| Remove duplicates | 9,692 | 5,753 |
| Remove missing salary | 9,127 | 565 |
| Filter Data Analyst | 1,322 | 7,805 |

### Final Dataset

The final dataset contains:

- **1,322 Data Analyst records**
- **12 columns**
- No missing values in the analyzed dataset

The cleaned dataset is stored in:

```text
Filee/clean_data.csv
```

---

## Visualizations

### Average Salary by Experience

![Average Salary by Experience](outputs/charts/salary_by_experience.png)

### Salary by Remote Working Ratio

![Salary by Remote Working Ratio](outputs/charts/salary_remote_working.png)

### Salary by Company Size

![Salary by Company Size](outputs/charts/salary_company_size.png)

---

# 🔎 Exploratory Data Analysis

## 1. Experience Level

The number of Data Analyst records by experience level:

| Experience | Count | Percentage |
|---|---:|---:|
| SE | 619 | 46.82% |
| MI | 355 | 26.85% |
| EN | 324 | 24.51% |
| EX | 24 | 1.82% |

The dataset is dominated by **Senior-level (SE)** Data Analysts, representing 46.82% of the final sample.

---

## 2. Company Size

| Company Size | Count | Percentage |
|---|---:|---:|
| M | 1,204 | 91.07% |
| L | 87 | 6.58% |
| S | 31 | 2.34% |

The majority of observations come from **medium-sized companies (M)**.

Therefore, comparisons involving large and small companies should be interpreted carefully because their sample sizes are substantially smaller.

---

## 3. Remote Working Ratio

| Remote Working Ratio | Count | Percentage |
|---|---:|---:|
| 0% | 765 | 57.87% |
| 100% | 518 | 39.18% |
| 50% | 39 | 2.95% |

Most observations represent **fully on-site positions (0%)**, followed by fully remote positions (100%).

---

# 💰 Salary Analysis

## Overall Salary Statistics

| Statistic | Salary (USD) |
|---|---:|
| Count | 1,322 |
| Mean | $106,095.37 |
| Standard Deviation | $53,862.90 |
| Minimum | $15,000 |
| Q1 | $70,000 |
| Median | $100,000 |
| Q3 | $133,000 |
| Maximum | $774,000 |

The salary distribution is influenced by several high-value observations, causing the mean to be higher than the median.

Therefore, both **mean and median** are considered when interpreting salary patterns.

---

# 📈 Salary by Experience

| Experience | Mean Salary | Median Salary | Count |
|---|---:|---:|---:|
| EN | $83,975.30 | $75,750 | 324 |
| MI | $95,275.40 | $86,400 | 355 |
| SE | $123,724.66 | $119,200 | 619 |
| EX | $110,072.92 | $115,000 | 24 |

The salary pattern generally increases from **Entry-level (EN)** to **Mid-level (MI)** and **Senior-level (SE)**.

Senior-level Data Analysts have the highest average salary among the major experience groups, at approximately **$123.7K**.

The Executive (EX) group has a relatively small sample size of only 24 observations, so its result should be interpreted cautiously.

---

# 🏢 Salary by Company Size

| Company Size | Mean Salary | Median Salary | Count |
|---|---:|---:|---:|
| M | $109,008.82 | $102,467 | 1,204 |
| L | $78,042.80 | $67,419 | 87 |
| S | $71,668.81 | $58,000 | 31 |

In this dataset, medium-sized companies have the highest average salary.

However, this result should not be interpreted as evidence that company size directly causes higher salaries because the dataset is observational and heavily dominated by medium-sized companies.

---

# 🏠 Remote Working Analysis

| Remote Working Ratio | Mean Salary | Median Salary | Count |
|---|---:|---:|---:|
| 0% | $107,751.59 | $100,000 | 765 |
| 100% | $107,270.01 | $101,750 | 518 |
| 50% | $58,006.51 | $51,519 | 39 |

The average salaries for fully on-site and fully remote positions are relatively similar.

The 50% remote category has a substantially lower average salary, but it contains only **39 observations**.

Therefore, remote working ratio should not be interpreted independently from other factors such as experience level, job role, company characteristics, and location.

---

# 🔬 Experience × Company Size

The analysis also compares salary across combinations of experience level and company size.

The results show that salary differences associated with company size are not consistent across all experience levels.

For example, Senior-level employees in medium-sized companies have an average salary of approximately **$124.5K**, while Senior-level employees in small companies have an average of approximately **$89.9K**.

This suggests that salary patterns can vary when multiple variables are considered simultaneously.

---

# 🏠 Experience × Remote Working

Salary was also analyzed by combining:

**Experience Level × Remote Working Ratio**

The results show that the relationship between remote working and salary is not consistent across experience groups.

For example:

- Senior-level, 0% remote: approximately $124.4K
- Senior-level, 100% remote: approximately $123.7K
- Mid-level, 0% remote: approximately $101.6K
- Mid-level, 100% remote: approximately $89.9K
- Entry-level, 0% remote: approximately $88.8K
- Entry-level, 100% remote: approximately $78.1K

This indicates that **experience level is an important factor to consider when interpreting remote working and salary patterns**.

---

# ⚠️ Outlier Analysis

Potential salary outliers were identified using the **Interquartile Range (IQR)** method.

### IQR Results

- Q1 = $70,000
- Q3 = $133,000
- IQR = $63,000
- Lower Bound = -$24,500
- Upper Bound = $227,500

A total of **19 potential outliers** were identified above the upper bound.

The highest salaries include:

| Experience | Salary |
|---|---:|
| EN | $774,000 |
| SE | $750,000 |
| MI | $430,967 |
| SE | $385,000 |
| MI | $369,120 |

These observations have a substantial effect on the overall salary mean.

For comparison:

- Mean salary including extreme values: **$106,095.37**
- Mean salary below $300,000: **$104,106.53**

The analysis does not automatically remove these observations because an outlier is not necessarily an error.

---

# 📊 Statistical Analysis

## Kruskal-Wallis Test

To evaluate whether salary distributions differ across experience levels, a **Kruskal-Wallis H test** was performed.

### Results

- **H-statistic:** 219.21
- **p-value:** < 0.001
- **Epsilon-squared:** 0.164

The result indicates a **statistically significant difference in salary distributions across experience groups**.

The effect size indicates that experience level is associated with a meaningful portion of the variation in salary ranks within this dataset.

However, statistical significance does not imply causation.

---

## Post-Hoc Analysis

Because the Kruskal-Wallis test showed a significant overall difference, pairwise **Mann-Whitney U tests** were performed.

A **Holm correction** was applied to control for multiple comparisons.

### Significant Differences

| Comparison | Adjusted p-value | Significant |
|---|---:|:---:|
| EN vs EX | 0.00385 | ✅ |
| EN vs MI | 0.00089 | ✅ |
| EN vs SE | < 0.001 | ✅ |
| MI vs SE | < 0.001 | ✅ |

### Not Statistically Significant

| Comparison | Adjusted p-value | Significant |
|---|---:|:---:|
| EX vs MI | 0.09365 | ❌ |
| EX vs SE | 0.25237 | ❌ |

The post-hoc results show that the strongest evidence of salary differences occurs between **Entry-level, Mid-level, and Senior-level groups**.

The Executive group does not show a statistically significant difference from the Mid-level and Senior-level groups after Holm correction.

Because the Executive group contains only 24 observations, these comparisons should be interpreted cautiously.

---

# 🧠 Key Findings

The main findings from the analysis are:

### 1. Experience is strongly associated with salary differences

Senior-level Data Analysts have the highest average salary among the major experience groups.

The Kruskal-Wallis test also indicates that salary distributions differ significantly across experience levels.

---

### 2. Salary distribution is right-skewed

The presence of several high salary observations increases the mean salary.

Therefore, median salary should also be considered when interpreting the typical salary level.

---

### 3. Medium-sized companies dominate the dataset

Approximately **91.07%** of the final observations come from medium-sized companies.

This makes conclusions about small and large companies less reliable due to their smaller sample sizes.

---

### 4. Remote working alone does not explain salary differences

Fully remote and fully on-site positions have relatively similar average salaries.

The differences become more complex when experience level is considered simultaneously.

---

### 5. Job designation can be associated with substantial salary differences

Some specialized Data Analyst designations show higher average salaries.

However, several designations have very small sample sizes, so their averages should not be treated as representative market benchmarks.

---

### 6. Salary outliers have a measurable impact

The dataset contains 19 potential outliers above the IQR upper bound.

The extreme values increase the overall mean, demonstrating why both mean and median are important for salary analysis.

---

# ⚠️ Limitations

Several limitations should be considered when interpreting this analysis:

- The dataset is based on publicly available data and may not represent the entire Data Analyst labor market.
- The sample is heavily concentrated in certain categories, particularly US-based companies and medium-sized companies.
- Several job designations and locations have very small sample sizes.
- Potential outliers may represent legitimate high salaries rather than data errors.
- The analysis is observational and therefore does not establish causal relationships.
- Salary can be influenced by additional factors such as location, industry, company, job responsibilities, education, and negotiation.
- Remote working ratio should not be interpreted as an independent cause of salary differences.
- Statistical significance indicates evidence of differences in the observed data, not causation.

---

# 🛠️ Tools & Technologies

This project uses:

- **Python** — programming language
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical computation
- **Matplotlib** — data visualization
- **Seaborn** — statistical visualization
- **SciPy** — statistical hypothesis testing
- **Flask** — web application / presentation layer

---

# 📁 Project Structure

```text
data-analyst-compensation-analysis/
│
├── Filee/
│   ├── DataScience_Salaries_And_Fields.csv
│   └── clean_data.csv
│
├── codee/
│   ├── intake.py
│   ├── clean.py
│   ├── analisis.py
│   └── grafik.py
│
├── outputs/
│   └── charts/
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 How to Run

1. Clone Repository

```
git clone https://github.com/Fatah-Tazaru/data-analyst-compensation-analysis.git
cd data-analyst-compensation-analysis
```

2. Install Dependencies

```
pip install -r requirements.txt
```

3. Run Data Intake

```
python codee/intake.py
```

This step checks the initial dataset structure, columns, data types, missing values, duplicate rows, unique values, and data consistency.

4. Run Data Cleaning

```
python codee/clean.py
```

This step removes unnecessary columns and duplicate rows, handles missing salary values, filters relevant Data Analyst records, and generates the cleaned dataset.

5. Run Exploratory Data Analysis

```
python codee/analisis.py
```

This step calculates descriptive statistics and analyzes salary patterns based on experience, company characteristics, and remote working.

6. Generate Visualizations

```
python codee/grafik.py
```

The generated charts are saved in:

```
outputs/charts/
```

7. Review the Results

The analysis results and visualizations can be reviewed through the generated output files and charts in the repository.

---

# 📈 Visualizations

The project includes visualizations for:

- Salary distribution
- Salary by experience
- Salary by designation
- Salary by company size
- Salary by remote working ratio
- Experience × company size
- Experience × remote working
- Salary outlier analysis

Visualizations are stored in:

```text
outputs/charts/
```

---

# 🌐 Flask Application

A Flask application is included as an additional presentation layer for the analysis.

The application presents selected salary analysis results through a simple web interface.

---

# 📌 Conclusion

This project demonstrates an end-to-end data analysis workflow using Python.

The analysis starts from raw data and proceeds through:

**Data Intake → Data Cleaning → Exploratory Analysis → Outlier Analysis → Statistical Testing → Visualization**

The findings suggest that **experience level is an important factor associated with salary differences among Data Analyst observations in this dataset**.

Senior-level Data Analysts have higher typical salaries than Entry-level and Mid-level groups, and the statistical analysis provides strong evidence that salary distributions differ across experience levels.

At the same time, salary should not be evaluated using experience alone. Company size, remote working, job designation, location, and other factors can also contribute to salary differences.

Therefore, this project treats the results as **observed patterns within the dataset rather than causal conclusions or definitive market benchmarks**.

---

## Limitations

- The dataset is a public dataset and may not represent the entire global Data Analyst job market.
- Salary distributions contain extreme values that can affect the mean.
- The analysis describes relationships and patterns in the dataset but does not establish causation.
- Geographic representation is uneven, with a large proportion of records coming from the United States.
- Salary values may vary depending on factors that are not fully captured in the dataset, such as industry, company, location, and specific responsibilities.

---

## 👤 Author

**Fatah-Tazaru**

Data Analyst Portfolio Project
