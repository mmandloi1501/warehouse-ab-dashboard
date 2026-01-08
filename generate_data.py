import pandas as pd
import numpy as np

np.random.seed(42)

days = 60
start_date = pd.to_datetime("2024-01-01")
orders_per_day_range = (80, 120)

warehouse_id = "WH_01"
pickers = [f"P_{i}" for i in range(1, 21)]

data = []
order_id = 1

for day in range(days):
    date = start_date + pd.Timedelta(days=day)
    daily_orders = np.random.randint(*orders_per_day_range)

    for _ in range(daily_orders):
        process_group = np.random.choice(["A", "B"])
        items_count = np.random.randint(1, 20)

        if process_group == "A":
            processing_time = np.random.normal(32, 6)
            labor_cost = np.random.normal(18, 3)
            error_flag = np.random.binomial(1, 0.06)
            on_time = np.random.binomial(1, 0.92)
        else:
            processing_time = np.random.normal(27, 5)
            labor_cost = np.random.normal(15, 2.5)
            error_flag = np.random.binomial(1, 0.03)
            on_time = np.random.binomial(1, 0.96)

        data.append([
            f"ORD_{order_id}",
            date.date(),
            process_group,
            warehouse_id,
            np.random.choice(pickers),
            items_count,
            max(processing_time, 5),
            max(labor_cost, 5),
            error_flag,
            on_time
        ])

        order_id += 1

columns = [
    "order_id",
    "order_date",
    "process_group",
    "warehouse_id",
    "picker_id",
    "items_count",
    "processing_time_min",
    "labor_cost",
    "error_flag",
    "on_time_delivery"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("warehouse_orders.csv", index=False)

print("warehouse_orders.csv created successfully!")
