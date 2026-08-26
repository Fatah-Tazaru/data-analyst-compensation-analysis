📊 Data Analyst Compensation Analysis

Analisis eksploratif mengenai kompensasi Data Analyst berdasarkan tingkat pengalaman, ukuran perusahaan, dan pola remote working menggunakan Python.

Project ini dibuat untuk memahami bagaimana karakteristik pekerjaan berhubungan dengan salary serta mengidentifikasi pola dan anomali pada data kompensasi.

---

🎯 Project Overview

Salary merupakan salah satu faktor penting dalam memahami kondisi pasar kerja Data Analyst.

Project ini menggunakan dataset salary untuk menjawab beberapa pertanyaan analitis dan membangun proses analisis dari raw data hingga insight.

Workflow project:

Raw Dataset
     ↓
Data Intake & Validation
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Outlier Analysis
     ↓
Data Visualization
     ↓
Key Findings

---

❓ Business Questions

Analisis ini berfokus pada beberapa pertanyaan:

1. Bagaimana distribusi salary Data Analyst?
2. Apakah salary berbeda berdasarkan experience level?
3. Bagaimana rata-rata dan median salary pada setiap experience level?
4. Apakah terdapat salary outlier yang ekstrem?
5. Bagaimana salary berbeda berdasarkan company size?
6. Apakah remote working ratio berhubungan dengan salary?
7. Apakah hubungan antara remote working dan salary tetap terlihat ketika experience level diperhitungkan?

---

📦 Dataset

Dataset yang digunakan berasal dari dataset salary Data Science yang kemudian difilter untuk memperoleh data yang relevan dengan posisi Data Analyst.

Dataset awal memiliki:

- 15,445 rows
- 13 columns

Beberapa kolom yang digunakan dalam analisis antara lain:

Column| Description
"Working_Year"| Tahun pekerjaan
"Designation"| Posisi pekerjaan
"Experience"| Experience level
"Employment_Status"| Status pekerjaan
"Employee_Location"| Lokasi employee
"Company_Location"| Lokasi perusahaan
"Company_Size"| Ukuran perusahaan
"Remote_Working_Ratio"| Persentase remote working
"salary_in_usd"| Salary dalam USD

---

🧹 Data Cleaning

Data cleaning dilakukan menggunakan "clean.py".

Tahapan utama:

1. Membaca dataset raw.
2. Menghapus kolom yang tidak diperlukan.
3. Menghapus duplicate rows.
4. Menghapus data yang tidak memiliki "salary_in_usd".
5. Memfilter data berdasarkan designation yang relevan dengan Data Analyst.
6. Menyimpan dataset hasil cleaning sebagai "clean_data.csv".

Data Cleaning Flow

Original Dataset
      ↓
Remove Unnecessary Columns
      ↓
Remove Duplicates
      ↓
Remove Missing Salary
      ↓
Filter Data Analyst Roles
      ↓
Clean Dataset

Outlier tidak langsung dihapus pada tahap cleaning karena outlier merupakan bagian yang perlu dianalisis secara terpisah.

---

🔎 Data Intake & Validation

Sebelum proses cleaning, dataset diperiksa menggunakan "intake.py".

Pemeriksaan meliputi:

- struktur dataset,
- jumlah rows dan columns,
- missing values,
- duplicate rows,
- unique values,
- distribusi kategori,
- serta konsistensi antara kolom salary.

Tahap ini dilakukan untuk memahami kondisi data sebelum menentukan strategi cleaning.

---

📊 Exploratory Data Analysis

Analisis dilakukan menggunakan "analisis.py".

Beberapa statistik yang digunakan:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation
- Quartile
- Count

Mean dan median digunakan secara bersamaan karena distribusi salary memiliki nilai ekstrem yang dapat memengaruhi rata-rata.

---

🚨 Outlier Analysis

Outlier dianalisis menggunakan metode Interquartile Range (IQR).

Formula:

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

Analisis ini digunakan untuk mengidentifikasi salary yang berada jauh dari distribusi utama.

Outlier tidak otomatis dianggap sebagai kesalahan data. Nilai tersebut terlebih dahulu diperlakukan sebagai bagian dari distribusi salary dan dianalisis dampaknya terhadap statistik.

---

💡 Key Findings

1. Experience dan Salary

Salary menunjukkan pola peningkatan berdasarkan experience level.

Dalam dataset hasil analisis, Senior-level ("SE") memiliki rata-rata salary sekitar $123.7K, sedangkan Entry-level ("EN") sekitar $84.0K.

Hal ini menunjukkan adanya hubungan positif antara experience level dan compensation.

---

2. Salary Distribution

Distribusi salary menunjukkan pola right-skewed.

Sebagian besar salary berada pada rentang yang lebih rendah, sementara terdapat sejumlah salary yang jauh lebih tinggi.

Karena itu, median digunakan bersama mean untuk memberikan gambaran distribusi yang lebih representatif.

---

3. Salary Outliers

Analisis IQR menemukan sejumlah salary yang berada jauh di atas distribusi utama.

Nilai ekstrem tersebut dapat memberikan pengaruh besar terhadap mean salary.

Oleh karena itu, kesimpulan mengenai salary tidak hanya didasarkan pada average salary.

---

4. Experience × Remote Working

Analisis juga membandingkan salary berdasarkan kombinasi:

Experience Level
        ×
Remote Working Ratio

Hasilnya menunjukkan bahwa perbedaan salary berdasarkan remote working tidak selalu konsisten ketika experience level diperhitungkan.

Hal ini menunjukkan bahwa experience perlu dipertimbangkan ketika membandingkan compensation berdasarkan remote working.

---

📈 Visualizations

Visualisasi dibuat menggunakan "grafik.py" dan disimpan pada:

outputs/charts/

Visualisasi digunakan untuk membantu memahami:

- Salary distribution
- Average salary berdasarkan experience
- Salary berdasarkan kategori pekerjaan
- Relationship antara experience dan salary
- Remote working dan salary
- Analisis distribusi serta outlier

---

🛠️ Tools & Technologies

Project ini menggunakan:

- Python
- Pandas — data manipulation dan analysis
- NumPy — numerical computation
- Matplotlib — data visualization
- Seaborn — statistical visualization
- Flask — web application / presentation layer

---

📁 Project Structure

```
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
│       ├── salary_distribution.png
│       └── ...
│
├── README.md
├── LICENSE
└── .gitignore
```
---

🚀 How to Run

Clone repository:

git clone https://github.com/Fatah-Tazaru/data-analyst-compensation-analysis.git

Masuk ke directory:

cd data-analyst-compensation-analysis

Install dependencies:

pip install pandas numpy matplotlib seaborn flask

Jalankan proses data intake:

python codee/intake.py

Jalankan data cleaning:

python codee/clean.py

Jalankan analisis:

python codee/analisis.py

Buat visualisasi:

python codee/grafik.py

---

⚠️ Limitations

Beberapa keterbatasan dalam analisis ini:

- Dataset berasal dari sumber publik sehingga belum tentu merepresentasikan seluruh pasar kerja Data Analyst.
- Salary memiliki outlier yang ekstrem.
- Jumlah observasi antar kategori dapat berbeda.
- Analisis ini bersifat observational sehingga hubungan antar variabel tidak dapat langsung dianggap sebagai hubungan sebab-akibat.
- Remote working ratio tidak dapat digunakan sendirian untuk menjelaskan perbedaan salary karena faktor lain seperti experience dan company size juga dapat berpengaruh.

---

📌 Conclusion

Analisis menunjukkan bahwa experience level memiliki pola yang jelas terhadap salary Data Analyst, dengan salary cenderung meningkat pada tingkat pengalaman yang lebih tinggi.

Selain itu, distribusi salary memiliki outlier dan skewness sehingga penggunaan mean dan median secara bersamaan menjadi penting.

Analisis remote working juga menunjukkan bahwa hubungan antara remote working dan salary perlu dilihat bersama faktor lain, terutama experience level.

Project ini menunjukkan proses analisis data mulai dari data intake, cleaning, exploratory analysis, outlier analysis, hingga visualization menggunakan Python.
