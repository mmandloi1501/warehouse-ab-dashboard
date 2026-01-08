# Warehouse Process A/B Testing Analysis

## 🚀 Project Overview
This project evaluates the efficiency and cost-effectiveness of two warehouse operational processes (Process A vs Process B).  
The goal is to identify which process reduces processing time and labor cost, using Python, SQL, statistical analysis, and data visualization.

This project demonstrates key skills for Operations Analyst and Supply Chain Analyst roles, including:

- Data extraction and manipulation using SQL and pandas
- Statistical analysis with A/B testing
- KPI calculation and business performance metrics
- Data visualization with Seaborn and Matplotlib
- Secure handling of credentials using `.env` files
- Presenting actionable insights for decision-making

---

## 📊 Dataset
- Simulated 60 days of warehouse orders
- Columns:
  | Column | Description |
  |--------|-------------|
  | `order_id` | Unique ID for each order |
  | `order_date` | Date of order |
  | `process_group` | Warehouse process (A or B) |
  | `warehouse_id` | Warehouse identifier |
  | `picker_id` | Employee who picked the order |
  | `items_count` | Number of items per order |
  | `processing_time_min` | Time taken to process order (minutes) |
  | `labor_cost` | Labor cost per order (€) |
  | `error_flag` | 1 if error occurred, 0 otherwise |
  | `on_time_delivery` | 1 if delivered on time, 0 otherwise |

---

## 🛠 Tools & Technologies
- Python for data analysis and visualization
- MySQL for storing and querying warehouse data
- pandas for data manipulation
- scipy.stats for A/B statistical tests
- Seaborn & Matplotlib for visualization
- dotenv for secure credential management
- Git & GitHub for version control and portfolio

---

## 🔍 Methodology
1. Data Extraction: Connected Python to MySQL database and imported warehouse order data.
2. Data Cleaning & Preview: Checked the first few rows of the dataset for consistency.
3. Group Splitting: Split orders into Process A and Process B groups.
4. KPI Calculation: Computed average processing time and labor cost for each group.
5. A/B Testing: Conducted two-sample t-tests to check if differences are statistically significant.
6. % Improvement: Calculated improvement of Process B over Process A in both metrics.
7. Visualization: Created bar charts and boxplots to highlight differences and distributions.
8. Interpretation: Provided actionable insights for warehouse management.

---

## 📈 Key Insights
- Processing Time: Process B reduced average processing time by ~X% compared to Process A.
- Labor Cost: Process B reduced labor cost by ~Y% compared to Process A.
- Statistical Significance: P-values < 0.05 indicate that differences are statistically significant.
- Distribution Analysis: Boxplots show Process B has fewer extreme delays and cost spikes.

Business Impact:  
> Implementing Process B can lead to faster warehouse operations, lower labor costs, and improved operational efficiency.

---

## 📊 Visualizations

### 1️⃣ Bar Chart: Average Metrics
Shows comparison of average processing time and labor cost between Process A and B.

### 2️⃣ Boxplot: Processing Time Distribution
Displays the spread, outliers, and variation in processing times for each process.

### 3️⃣ Boxplot: Labor Cost Distribution
Displays the spread, outliers, and variation in labor cost for each process.

(Charts generated in Python using Seaborn & Matplotlib)

---

## 💡 Resume / Portfolio Takeaways
- Conducted end-to-end A/B testing analysis using real operational metrics
- Calculated KPIs and percentage improvement to quantify efficiency gains
- Built interactive, visual analytics to communicate results effectively
- Secured sensitive credentials using environment variables
- Skills demonstrated: SQL, Python, pandas, statistical testing, data visualization, supply chain/operations analysis

---

## 🔐 Security
- Database credentials are stored securely in a `.env` file
- `.env` is ignored in `.gitignore` to prevent public exposure

---

## 📂 Project Structure
Warehouse_AB_Test/
├── ab_testing.py # Main Python script
├── warehouse_orders.csv # Simulated warehouse dataset
├── .env # Hidden database credentials (not uploaded)
├── .gitignore # To ignore sensitive files
└── README.md # Project description and methodology


