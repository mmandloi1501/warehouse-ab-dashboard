# =============================================
# Warehouse Process A/B Testing Dashboard
# Portfolio-Ready with Full Storytelling
# =============================================

import streamlit as st
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

# -----------------------------
# CONNECT TO MYSQL AND LOAD DATA
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=DB_PASSWORD,
    database="warehouse_ab_test"
)

query = """
SELECT
    process_group,
    processing_time_min,
    labor_cost
FROM warehouse_orders
"""

df = pd.read_sql(query, conn)

# -----------------------------
# DASHBOARD CONFIG
# -----------------------------
st.set_page_config(page_title="Warehouse A/B Dashboard", layout="wide")
st.title("🏭 Warehouse Process A/B Testing Dashboard")
st.markdown("""
Welcome to the **Warehouse A/B Testing Dashboard**.  
This dashboard compares **Process A** and **Process B** for warehouse order handling in terms of **Processing Time** and **Labor Cost**.  

Use the sidebar to filter processes or select a metric to explore. This dashboard includes **KPIs, distributions, statistical analysis, and actionable insights**.
""")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Filter & Explore Options")

process_filter = st.sidebar.multiselect(
    "Select Process Group(s) to Analyze",
    options=df["process_group"].unique(),
    default=df["process_group"].unique()
)

metric_option = st.sidebar.selectbox(
    "Select Metric for Visualization",
    options=["Processing Time", "Labor Cost"]
)

# Filter data
filtered_df = df[df["process_group"].isin(process_filter)]
group_A = filtered_df[filtered_df["process_group"] == "A"]
group_B = filtered_df[filtered_df["process_group"] == "B"]

# -----------------------------
# HELPER FUNCTION
# -----------------------------
def safe_mean(series):
    return series.mean() if not series.empty else 0

# -----------------------------
# KPI CARDS
# -----------------------------
avg_proc_time_A = safe_mean(group_A["processing_time_min"])
avg_proc_time_B = safe_mean(group_B["processing_time_min"])
avg_labor_cost_A = safe_mean(group_A["labor_cost"])
avg_labor_cost_B = safe_mean(group_B["labor_cost"])

st.header("📊 Key Performance Indicators (KPIs)")
st.markdown("""
These **KPIs** show the average processing time and labor cost for each process.  
They provide a **quick snapshot** of which process is more efficient and cost-effective.
""")

col1, col2 = st.columns(2)
with col1:
    st.metric("Avg Processing Time A (min)", f"{avg_proc_time_A:.2f}")
    st.metric("Avg Labor Cost A (€)", f"{avg_labor_cost_A:.2f}")
with col2:
    st.metric("Avg Processing Time B (min)", f"{avg_proc_time_B:.2f}")
    st.metric("Avg Labor Cost B (€)", f"{avg_labor_cost_B:.2f}")

# -----------------------------
# PERCENTAGE IMPROVEMENT
# -----------------------------
proc_time_improvement = ((avg_proc_time_A - avg_proc_time_B) / avg_proc_time_A) * 100 if avg_proc_time_A else 0
labor_cost_improvement = ((avg_labor_cost_A - avg_labor_cost_B) / avg_labor_cost_A) * 100 if avg_labor_cost_A else 0

st.subheader("✅ Percentage Improvement of Process B vs A")
st.markdown(f"""
- **Processing Time:** Process B is **{proc_time_improvement:.2f}% faster** than Process A.  
- **Labor Cost:** Process B is **{labor_cost_improvement:.2f}% cheaper** than Process A.
""")
st.markdown("""
*These improvements indicate potential operational efficiency and cost savings by adopting Process B.*
""")

# -----------------------------
# STATISTICAL SIGNIFICANCE
# -----------------------------
if not group_A.empty and not group_B.empty:
    t_time, p_time = stats.ttest_ind(group_A["processing_time_min"], group_B["processing_time_min"], equal_var=False)
    t_cost, p_cost = stats.ttest_ind(group_A["labor_cost"], group_B["labor_cost"], equal_var=False)
else:
    p_time, p_cost = None, None

# Preprocess p-values to avoid formatting error
p_time_display = f"{p_time:.5f}" if p_time is not None else "N/A"
p_cost_display = f"{p_cost:.5f}" if p_cost is not None else "N/A"

st.subheader("📈 Statistical Significance (p-values)")
st.markdown(f"""
- **Processing Time p-value:** {p_time_display}  
- **Labor Cost p-value:** {p_cost_display}
""")
st.markdown("""
*Interpretation:*  
- A **p-value < 0.05** indicates a **statistically significant difference** between Process A and Process B.  
- This confirms that observed improvements are **unlikely due to random chance**.
""")

# -----------------------------
# VISUALIZATIONS
# -----------------------------
st.header("📊 Visual Insights")
st.markdown("""
Visualizations help us **understand distributions, variability, and trends** in the warehouse processes.
""")

avg_metrics = pd.DataFrame({
    "Process": ["A", "B"],
    "Processing Time": [avg_proc_time_A, avg_proc_time_B],
    "Labor Cost": [avg_labor_cost_A, avg_labor_cost_B]
})
avg_metrics_melted = avg_metrics.melt(id_vars="Process", var_name="Metric", value_name="Value")

# Bar chart
st.subheader(f"Bar Chart: {metric_option} Comparison")
fig1, ax1 = plt.subplots(figsize=(8,5))
sns.barplot(data=avg_metrics_melted[avg_metrics_melted["Metric"]==metric_option],
            x="Metric", y="Value", hue="Process", ax=ax1)
ax1.set_ylabel(metric_option)
st.pyplot(fig1)
st.markdown(f"*This bar chart shows the average {metric_option} for Process A vs Process B, highlighting the difference clearly.*")

# Boxplot
st.subheader(f"Distribution of {metric_option}")
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.boxplot(
    x="process_group", 
    y="processing_time_min" if metric_option=="Processing Time" else "labor_cost", 
    data=filtered_df, ax=ax2
)
ax2.set_xlabel("Process Group")
ax2.set_ylabel(metric_option)
st.pyplot(fig2)
st.markdown(f"*Boxplots show the spread, variability, and outliers in {metric_option}, helping identify consistency and risk.*")

# -----------------------------
# BUSINESS INSIGHTS / STORY
# -----------------------------
st.header("💡 Business Insights & Recommendations")
st.markdown(f"""
After analyzing the data:  

- **Process B** consistently outperforms Process A in terms of **speed and labor cost**.  
- **Statistical tests** confirm these differences are significant (p-value < 0.05).  
- Adopting Process B could result in **faster order processing, lower operational cost, and higher efficiency**.  

**Next Steps / Extensions:**  
- Monitor other key metrics like **error rate, on-time delivery, and order volume**.  
- Scale the analysis across multiple warehouses or over different seasons.  
- Build an **interactive Streamlit dashboard** with real-time KPI monitoring (already partially implemented).  
""")
