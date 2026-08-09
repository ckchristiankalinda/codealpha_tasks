# 🌍 Global Sales Analysis — Power BI Dashboard

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=flat&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)


A 3-page Power BI dashboard analyzing global retail performance across 7 markets and 4 years, built on the Global Superstore dataset (51,290 transactions, 2011–2014). The project combines a full data quality audit, DAX-driven KPIs, and a business-ready storytelling layer to answer one question: **where is the business winning, and where is it quietly losing money?**

---

## 📌 Business Objective

Global Superstore's leadership needs a single source of truth to monitor global sales performance and identify where profitability is at risk — by market, product, customer, and discount behavior — in order to prioritize corrective action.

---

## 🗂️ Repository Structure

```
global-sales-analysis-dashboard/
├── README.md
├── data/
│   └── processed/
│       └── Global_Superstore_Cleaned.csv     # Cleaned dataset (51,280 rows, audit-passed)
├── docs/
│   └── Data_Quality_Report.md                # Full data quality audit & cleaning rationale
├── scripts/
│   └── clean_superstore.py                   # Reproducible Python cleaning pipeline
├── images/
  
```

> **Note:** the raw source file is not included in this repository to keep it lightweight. The full cleaning pipeline (`scripts/clean_superstore.py`) is fully reproducible against the original Global Superstore CSV.

---

## 🧹 Data Quality & Cleaning

Before any visual was built, the dataset went through a full audit. Key findings and fixes are documented in [`docs/Data_Quality_Report.md`](docs/Data_Quality_Report.md):

| Issue | Impact | Action |
|---|---|---|
| `Product.ID` linked to multiple `Product.Name` values | 457 IDs / 4,392 rows (8.6%) | Harmonized to canonical name per ID |
| Austria & Mongolia misclassified under EMEA market | 97 rows | Reclassified to EU/Central and APAC/North Asia |
| Exact duplicate order lines | 10 rows | Removed |
| Inconsistent typographic quotes in product names | 811 rows | Standardized |
| Extreme discounts (≥70%) and statistical outliers | 2,104 / 7,363 rows | Flagged for review, not deleted (legitimate B2B activity) |

Result: **51,290 → 51,280 rows**, with full referential and geographic integrity restored — no data was blindly deleted; edge cases are preserved and flagged for business review.

---

## 📊 Dashboard Structure

### Page 1 — Global Sales Overview
KPI summary (Sales, Profit, Margin, Orders, Avg Discount), interactive world map by country, year-over-year trend, category and market breakdown, and market growth comparison (2011 → 2014).

### Page 2 — Profitability & Risk Analysis
![Profitability & Risk Analysis page](images/dashboard_page_2.png)

Profit by sub-category (isolating the one structurally unprofitable line), shipping mode cost/profit breakdown, top loss-making countries, top customers by profit, and a discount-vs-profit scatter analysis — with interactive Segment and Discount-range slicers.

### Page 3 — Key Observations & Recommendations
A synthesis page translating the analysis into a management-ready narrative: key findings on one side, prioritized action items on the other.

---

## 🔑 Key Insights

- Global sales grew from **$2.26M (2011)** to **$4.30M (2014)**, but growth is uneven: EU (+118%) and Africa (+122%) far outpace the US (+52%).
- **24.5% of order lines are sold at a loss**, totaling **-$920,634**.
- **"Tables"** is the only sub-category that loses money overall (**-$64,083**), masked by healthy performance elsewhere in Furniture.
- **Turkey (-$98,447)** and **Nigeria (-$80,751)** are the two most loss-making countries — together outweighing the Tables loss.
- Discount and profit are negatively correlated (**-0.32**); losses concentrate sharply above 70% discount.
- Premium shipping (First Class, Same Day) costs **~2x more per order** (~$41-43) than Standard Class (~$20).
- Customer profit concentration is moderate: the **top 20% of customers generate 43%** of total profit.

Full recommendations are detailed on the dashboard's **Key Observations & Recommendations** page.

---

## 🛠️ Tech Stack

- **Power BI Desktop** — data modeling, DAX measures, visuals
- **Python (pandas)** — data profiling, audit, and cleaning pipeline
- **DAX** — 10+ measures including time intelligence (YoY growth), referential and margin calculations

---

## ▶️ How to Reproduce

1. Clone this repository.
2. (Optional) Re-run the cleaning pipeline against a fresh copy of the raw Global Superstore CSV:
   ```bash
   pip install pandas
   python scripts/clean_superstore.py
   ```
3. Open Power BI Desktop and import `data/processed/Global_Superstore_Cleaned.csv` as the data source.
4. Rebuild the calendar table and DAX measures as documented in `docs/`.

---

## 👤 Author

**CK (Mutia Kalinda Christian)** — Data Analyst
Based in Kampala, Uganda | Portfolio project

---


