‎📊 Data Analyst Compensation & Salary Structure Analysis
‎
‎Proyek portofolio Data Analysis & Engineering berbasis Python ini menganalisis variabel-variabel yang memengaruhi kompensasi profesi Data Analyst secara global.
‎
‎📁 Project Structure
‎
‎￼
‎coba/
‎│
‎├── Filee/
‎│   ├── DataScience_Salaries_And_Fields.csv
‎│   └── clean_data.csv
‎│
‎├── codee/
‎│   ├── intake.py
‎│   ├── clean.py
‎│   ├── analisis.py
‎│   └── grafik.py
‎│
‎├── outputs/
‎│   ├── charts/
‎│   │   ├── salary_distribution.png
‎│   │   ├── average_salary_by_experience.png
‎│   │   ├── count_by_experience.png
‎│   │   ├── salary_boxplot_by_experience.png
‎│   │   ├── salary_experience_company_heatmap.png
‎│   │   ├── top_company_location_count.png
‎│   │   └── salary_experience_remote_heatmap.png
‎│   └── reports/
‎│
‎└── README.md
‎
‎💡 Key Business Insights
‎ * Pengalaman Kerja: Memiliki hubungan positif terkuat dengan kenaikan gaji (EN: ~$84K ➔ SE: ~$123.7K).
‎ * Distribusi Gaji: bersifat right-skewed akibat keberadaan outlier bernilai tinggi hingga $774K.
‎ * Ukuran Perusahaan: Perusahaan skala Medium (M) memberikan rata-rata gaji tertinggi ($109,009) dan mendominasi pasar.
‎ * Remote Ratio: Variabel 0% dan 100% remote tidak menunjukkan perbedaan gaji yang signifikan.
‎📈 Visualizations
‎| Visualisasi | Chart |
‎|---|---|
‎| Distribusi Gaji |  |
‎| Gaji vs Experience |  |
‎| Heatmap Company Size |  |
‎| Heatmap Remote |  |
‎🛠️ How to Run
‎python codee/clean.py
‎python codee/analisis.py
‎python codee/grafik.py
