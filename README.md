# 📦 Warehouse Process A/B Testing Analysis

> A rigorous statistical analysis comparing two warehouse operational processes — using Python, SQL, and A/B testing to identify which process delivers faster throughput and lower labour costs.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![MySQL](https://img.shields.io/badge/Database-MySQL-orange)](https://mysql.com)
[![SciPy](https://img.shields.io/badge/Stats-SciPy-purple)](https://scipy.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()

---

## 📌 The Business Problem

Warehouse operations teams often rely on gut feeling when choosing between operational processes — without statistical evidence to back up the decision. The wrong choice can cost thousands in unnecessary labour hours and delays.

**This project solves that problem** by applying rigorous A/B testing methodology to compare two warehouse processes across processing time, labour cost, error rates, and on-time delivery — giving operations managers statistically backed evidence to make the right call.

---

## 💡 Key Business Findings

| Metric | Process A | Process B | Improvement |
|--------|-----------|-----------|-------------|
| Avg Processing Time | X mins | Y mins | ~X% faster |
| Avg Labour Cost | €X | €Y | ~Y% cheaper |
| Statistical Significance | — | — | p-value < 0.05 ✅ |
| Error Rate | X% | Y% | Fewer errors |
| On-time Delivery | X% | Y% | Higher reliability |

> **Business Recommendation:** Implementing Process B across all warehouse operations delivers statistically significant improvements in speed and cost — directly impacting SLA compliance and operational efficiency.

---

## 🔍 What is A/B Testing?

A/B testing is a statistical method for comparing two versions of a process to determine which performs better — widely used in operations, product management, and marketing.

```
All warehouse orders (60 days)
           ↓
    ┌──────────────┐
    │   Split by   │
    │ process group│
    └──────────────┘
         ↙        ↘
  Process A      Process B
  (Control)     (Variant)
         ↘        ↙
    Statistical comparison
    (t-test, p-value < 0.05)
           ↓
    Business recommendation
```

A **p-value below 0.05** means the difference between the two processes is statistically significant — not due to random chance.

---

## 📊 Dataset

60 days of simulated warehouse order data with 10 operational variables:

| Column | Description |
|--------|-------------|
| `order_id` | Unique order identifier |
| `order_date` | Date of order |
| `process_group` | Warehouse process — A or B |
| `warehouse_id` | Warehouse identifier |
| `picker_id` | Employee who picked the order |
| `items_count` | Number of items per order |
| `processing_time_min` | Time taken to process order (minutes) |
| `labor_cost` | Labour cost per order (€) |
| `error_flag` | 1 if error occurred, 0 if clean |
| `on_time_delivery` | 1 if delivered on time, 0 if late |

---

## 🔍 Methodology

```
Step 1 — Data Extraction
Connect Python to MySQL and import 60 days of warehouse orders
        ↓
Step 2 — Data Cleaning
Check for nulls, inconsistencies and data quality issues
        ↓
Step 3 — Group Splitting
Separate orders into Process A (control) and Process B (variant)
        ↓
Step 4 — KPI Calculation
Compute average processing time and labour cost per group
        ↓
Step 5 — A/B Statistical Testing
Run two-sample t-tests to validate significance (p-value < 0.05)
        ↓
Step 6 — Improvement Calculation
Quantify % improvement of Process B over Process A
        ↓
Step 7 — Visualisation
Bar charts and boxplots to communicate findings clearly
        ↓
Step 8 — Business Recommendation
Actionable insight for warehouse management decision making
```

---

## 📈 Visualisations

### 1. Bar Chart — Average Metrics Comparison
Side-by-side comparison of average processing time and labour cost between Process A and B — instantly shows which process wins on each metric.

### 2. Boxplot — Processing Time Distribution
Shows the spread, outliers and variation in processing times for each process — Process B shows fewer extreme delays and tighter distribution.

### 3. Boxplot — Labour Cost Distribution
Shows cost spread and outliers per process — Process B shows fewer cost spikes and more consistent performance.

---

## 🛠️ Tools & Technologies

| Category | Tools Used |
|----------|-----------|
| Language | Python 3.11 |
| Database | MySQL |
| Data Processing | Pandas, NumPy |
| Statistical Testing | SciPy (two-sample t-test) |
| Visualisation | Seaborn, Matplotlib |
| Security | Python dotenv — credential management |
| Version Control | GitHub |

---

## 🔐 Security & Best Practices

- Database credentials stored securely in a `.env` file
- `.env` added to `.gitignore` — never exposed publicly
- Demonstrates professional handling of sensitive credentials
- Follows industry standard security practices for data projects

---

## 📁 Project Structure

```
warehouse-ab-testing/
│
├── ab_testing.py                 # Main analysis script
├── warehouse_orders.csv          # Simulated warehouse dataset
├── .env                          # Database credentials (hidden)
├── .gitignore                    # Prevents credential exposure
└── README.md                     # You are here!
```

---

## 🚀 How to Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/mmandloi1501/warehouse-ab-testing.git
cd warehouse-ab-testing
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Set up your .env file**
```bash
DB_HOST=your_host
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

**Step 4 — Run the analysis**
```bash
python ab_testing.py
```

---

## 💼 Skills Demonstrated

| Skill | How it's shown |
|-------|---------------|
| SQL | Data extraction from MySQL database |
| Python | End-to-end analysis pipeline |
| Statistical Analysis | Two-sample t-test, p-value interpretation |
| A/B Testing | Controlled experiment design and evaluation |
| KPI Design | Processing time, labour cost, error rate, on-time delivery |
| Data Visualisation | Bar charts and boxplots with Seaborn and Matplotlib |
| Operations Analytics | Warehouse process optimisation and efficiency analysis |
| Security best practices | Credential management with dotenv |

---

## 📈 What I Learned

- How to design and execute a statistically rigorous A/B test on operational data
- How to connect Python to a MySQL database and extract data programmatically
- How to interpret p-values and statistical significance for business decision making
- How to communicate complex statistical findings as clear business recommendations
- How to handle sensitive database credentials securely using environment variables
- How distribution analysis (boxplots) reveals operational inconsistencies beyond averages

---

## 🔗 Related Projects

| Project | Description |
|---------|-------------|
| [Smart Factory Analytics Platform](YOUR-SMART-FACTORY-URL-HERE) | Multi-module dashboard covering production, sales and recruitment |
| [Supply Chain Delay Predictor](https://supply-chain-delay-predictor-jsugpzbttfwgtnsynmfz7r.streamlit.app) | ML model predicting delivery delays on 100k+ orders |
| [OEE Calculator](YOUR-OEE-URL-HERE) | Live manufacturing efficiency calculator |
| [E-Commerce Dashboard](YOUR-ECOMMERCE-URL-HERE) | Sales and RFM customer segmentation dashboard |

---

## 👤 About Me

**Mohit Mandloi** — Business Analyst & Operations Analytics Professional

MSc Business Analytics | TUS Ireland | Production Management | Supply Chain Analytics

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/mmandloi1501)
[![Supply Chain](https://img.shields.io/badge/Supply_Chain-Delay_Predictor-orange)](https://supply-chain-delay-predictor-jsugpzbttfwgtnsynmfz7r.streamlit.app)
[![OEE App](https://img.shields.io/badge/OEE-Calculator-green)]

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

*If you found this project useful or interesting, please consider giving it a ⭐ on GitHub!*
