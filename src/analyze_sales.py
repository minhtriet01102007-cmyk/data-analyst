from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "sales_2025.csv"
OUT = ROOT / "data" / "processed"
REPORT = ROOT / "reports"

OUT.mkdir(exist_ok=True)
REPORT.mkdir(exist_ok=True)

df = pd.read_csv(RAW, encoding="utf-8-sig")
df["order_date"] = pd.to_datetime(df["order_date"])
df["profit"] = df["revenue"] - df["cost"]
df["margin"] = df["profit"] / df["revenue"]

# KPI
kpi = pd.DataFrame({
    "metric": ["orders", "units_sold", "revenue", "profit", "profit_margin"],
    "value": [
        df["order_id"].nunique(),
        df["quantity"].sum(),
        df["revenue"].sum(),
        df["profit"].sum(),
        df["profit"].sum() / df["revenue"].sum()
    ]
})
kpi.to_csv(OUT / "kpi.csv", index=False)

# Monthly analysis
monthly = (
    df.assign(month=df["order_date"].dt.to_period("M").astype(str))
      .groupby("month", as_index=False)
      .agg(revenue=("revenue","sum"), profit=("profit","sum"))
)
monthly.to_csv(OUT / "monthly_performance.csv", index=False)

# Product analysis
product = (
    df.groupby(["product_id","product_name","category"], as_index=False)
      .agg(units_sold=("quantity","sum"),
           revenue=("revenue","sum"),
           profit=("profit","sum"))
      .sort_values("revenue", ascending=False)
)
product.to_csv(OUT / "product_performance.csv", index=False)

# Channel analysis
channel = (
    df.groupby("channel", as_index=False)
      .agg(orders=("order_id","nunique"),
           revenue=("revenue","sum"),
           profit=("profit","sum"))
      .sort_values("revenue", ascending=False)
)
channel.to_csv(OUT / "channel_performance.csv", index=False)

# City analysis
city = (
    df.groupby("city", as_index=False)
      .agg(revenue=("revenue","sum"),
           profit=("profit","sum"))
      .sort_values("revenue", ascending=False)
)
city.to_csv(OUT / "city_performance.csv", index=False)

# Charts
plt.figure(figsize=(10,5))
plt.plot(monthly["month"], monthly["revenue"], marker="o")
plt.title("Monthly Revenue - 2025")
plt.xlabel("Month")
plt.ylabel("Revenue (VND)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(REPORT / "monthly_revenue.png", dpi=150)
plt.close()

plt.figure(figsize=(9,5))
top = product.head(10).sort_values("revenue")
plt.barh(top["product_name"], top["revenue"])
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (VND)")
plt.tight_layout()
plt.savefig(REPORT / "top_products.png", dpi=150)
plt.close()

print("Analysis completed.")
print(kpi.to_string(index=False))

