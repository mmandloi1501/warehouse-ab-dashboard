# =============================================
# Warehouse Process A/B Testing Analysis
# =============================================
# Author: Mohit
# Objective: Evaluate two warehouse processes (A vs B) in terms of
# efficiency (processing time) and cost (labor cost) using Python, SQL, 
# and statistical A/B testing.
# =============================================

# -----------------------------
# STEP 1: LOAD ENVIRONMENT VARIABLES
# -----------------------------
# We store sensitive information (like database password) in a .env file
# to avoid exposing it in the code, especially for GitHub or public sharing.
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file into environment

# -----------------------------
# STEP 2: CONNECT TO MYSQL DATABASE
# -----------------------------
# Connect to local MySQL warehouse database using hidden password
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),  # Safe: password hidden in .env
    database="warehouse_ab_test"
)

# -----------------------------
# STEP 3: QUERY DATA FROM MYSQL
# -----------------------------
# Fetch process group, processing time, and labor cost from the table
query = """
SELECT
    process_group,
    processing_time_min,
    labor_cost
FROM warehouse_orders
"""

# Load SQL query results into a pandas DataFrame
df = pd.read_sql(query, conn)

# Preview the first 5 rows to ensure data is loaded correctly
print("\nData loaded successfully!")
print(df.head())

# -----------------------------
# STEP 4: SPLIT DATA INTO GROUPS A AND B
# -----------------------------
# Separate the dataset into Process A and Process B for comparison
from scipy import stats

group_A = df[df["process_group"] == "A"]
group_B = df[df["process_group"] == "B"]

# -----------------------------
# STEP 5: CALCULATE AVERAGE METRICS
# -----------------------------
# Calculate the average processing time and labor cost for each process
print("\nAverage Processing Time (minutes)")
print("A:", round(group_A["processing_time_min"].mean(), 2))
print("B:", round(group_B["processing_time_min"].mean(), 2))

print("\nAverage Labor Cost (€)")
print("A:", round(group_A["labor_cost"].mean(), 2))
print("B:", round(group_B["labor_cost"].mean(), 2))

# -----------------------------
# STEP 6: PERFORM STATISTICAL A/B TEST
# -----------------------------
# Use two-sample t-tests to check if differences between A & B are statistically significant
# null hypothesis: no difference between groups
t_time, p_time = stats.ttest_ind(
    group_A["processing_time_min"],
    group_B["processing_time_min"],
    equal_var=False
)

t_cost, p_cost = stats.ttest_ind(
    group_A["labor_cost"],
    group_B["labor_cost"],
    equal_var=False
)

print("\nP-values")
print("Processing Time:", round(p_time, 5))
print("Labor Cost:", round(p_cost, 5))

# Interpretation:
# - p-value < 0.05: difference is statistically significant (real improvement)
# - p-value >= 0.05: difference may be due to random chance

# -----------------------------
# STEP 7: CALCULATE % IMPROVEMENT
# -----------------------------
# Calculate how much better Process B is compared to Process A
proc_time_improvement = ((group_A["processing_time_min"].mean() - group_B["processing_time_min"].mean()) / group_A["processing_time_min"].mean()) * 100
labor_cost_improvement = ((group_A["labor_cost"].mean() - group_B["labor_cost"].mean()) / group_A["labor_cost"].mean()) * 100

print("\nPercentage Improvement")
print("Processing Time Improvement: {:.2f}%".format(proc_time_improvement))
print("Labor Cost Improvement: {:.2f}%".format(labor_cost_improvement))

# -----------------------------
# STEP 8: VISUALIZATION OF RESULTS
# -----------------------------
# Visualizations make the results easier to understand for stakeholders

import matplotlib.pyplot as plt
import seaborn as sns

# ---------- 8a: BAR CHART FOR AVERAGE METRICS ----------
# Shows average processing time and labor cost for both processes
avg_metrics = pd.DataFrame({
    "Process": ["A", "B"],
    "Processing Time": [group_A["processing_time_min"].mean(), group_B["processing_time_min"].mean()],
    "Labor Cost": [group_A["labor_cost"].mean(), group_B["labor_cost"].mean()]
})

# Reshape data for Seaborn plotting
avg_metrics_melted = avg_metrics.melt(id_vars="Process", var_name="Metric", value_name="Value")

plt.figure(figsize=(8,5))
sns.barplot(data=avg_metrics_melted, x="Metric", y="Value", hue="Process")
plt.title("A vs B: Average Processing Time & Labor Cost")
plt.ylabel("Value")
plt.xlabel("Metric")
plt.legend(title="Process")
plt.show()

# ---------- 8b: BOXPLOT FOR PROCESSING TIME ----------
# Shows distribution, outliers, and spread of processing time
plt.figure(figsize=(10,5))
sns.boxplot(x="process_group", y="processing_time_min", data=df)
plt.title("Processing Time Distribution: A vs B")
plt.xlabel("Process Group")
plt.ylabel("Processing Time (min)")
plt.show()

# ---------- 8c: BOXPLOT FOR LABOR COST ----------
# Shows distribution, outliers, and spread of labor cost
plt.figure(figsize=(10,5))
sns.boxplot(x="process_group", y="labor_cost", data=df)
plt.title("Labor Cost Distribution: A vs B")
plt.xlabel("Process Group")
plt.ylabel("Labor Cost (€)")
plt.show()

# -----------------------------
# STEP 9: INTERPRETATION NOTES
# -----------------------------
# 1. Process B has lower average processing time → faster warehouse operations
# 2. Process B has lower labor cost → more cost-efficient
# 3. P-values < 0.05 → differences are statistically significant
# 4. Boxplots confirm B has fewer extreme delays and cost spikes
# 5. Percentage improvement highlights impact in business terms
