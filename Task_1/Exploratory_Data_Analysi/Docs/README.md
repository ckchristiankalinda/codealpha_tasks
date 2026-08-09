<h1 align="center">📊 Superstore Sales & Profitability Analysis</h1>
<p align="center"><b>A business-focused exploratory data analysis (EDA) turning four years of retail transactions into clear, actionable recommendations.</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen" alt="Status">
 
</p>

---

## 📌 Table of Contents

- [Business Context](#-business-context)
- [Project Objective](#-project-objective)
- [Dataset](#-dataset)
- [Key Business Insights](#-key-business-insights)
- [Strategic Recommendations](#-strategic-recommendations)
- [Repository Structure](#-repository-structure)
- [Tools & Technologies](#-tools--technologies)
- [About the Author](#-about-the-author)


---

## 🏢 Business Context

This project analyzes **51,290 retail transactions** from a global superstore operating across **147 countries**, between **2011 and 2014**. The company sells products across three categories — Technology, Furniture, and Office Supplies — and the leadership team wants to know one thing: **where is the business actually making money, where is it losing money, and what should be done about it?**

Rather than stopping at charts and numbers, this project reads every visualization the way a business consultant would present it in a boardroom: what the chart shows, what it means for the business, and what action it justifies.

## 🎯 Project Objective

Turn raw transactional data into a decision-ready business report by:
1. Identifying which products, categories, countries, and customer segments drive **revenue** vs. **profit** (they are not always the same).
2. Quantifying the real impact of discounting on profitability.
3. Uncovering seasonal patterns that can be used for planning and forecasting.
4. Delivering a clear set of prioritized, evidence-based business recommendations — in plain, non-technical language.

## 🗂 Dataset

| | |
|---|---|
| **Source** | `data/superstore.csv` |
| **Rows** | 51,290 transactions |
| **Time period** | January 2011 – December 2014 |
| **Coverage** | 147 countries, 3 categories, 17 sub-categories, 3,788 products |
| **Key fields** | Order Date, Category, Sub-Category, Sales, Profit, Discount, Quantity, Shipping Cost, Customer, Segment, Country, Region, Market |

## 💡 Key Business Insights

> Every finding below is backed by exact figures calculated directly from the dataset — no estimates, no assumptions.

### 1. Discounting above 30% is close to a guaranteed loss
Sales with no discount almost never lose money. But once a discount goes above 30%, **9 out of 10 of those sales lose money** for the business. Overall, **1 in 4 transactions in the entire dataset is unprofitable** — and discounting is the clearest reason why.

<img src="images/discount_vs_profit.png" alt="Discount vs Profit scatter plot" width="600">

### 2. Technology is the profit engine — Furniture is not
Technology drives **37.5% of sales but 45.2% of profit** — it converts revenue into profit better than any other category. Furniture sells almost as much as Technology (with nearly the same number of orders) but earns only **about half the profit per dollar sold**.

<img src="images/profit_by_category.png" alt="Profit by Category" width="600">

### 3. One product line is quietly losing money: Tables
Across all 17 product lines, **Tables is the only one that loses money overall** — a $64,083 loss on $757,034 in sales. Every other product line, even small ones, is profitable.

<img src="images/sales_vs_profit_by_subcategory.png" alt="Sales vs Profit by Sub-Category" width="600">

### 4. Revenue is geographically concentrated
Just **10 countries (out of 147) generate almost two-thirds of all sales**, led by the United States at 18% of global revenue. Selling a lot doesn't always mean earning a lot either — China and India convert sales into profit more efficiently than the higher-selling Australia.

<img src="images/top10_countries_by_sales.png" alt="Top 10 Countries by Sales" width="600">

### 5. Sales follow a reliable, repeatable yearly pattern
Every single year in the data shows the same rhythm: **February is always the slowest month**, and **November–December are always the busiest**. Combined with steady year-over-year growth (sales nearly doubled from 2011 to 2014), this is a pattern the business can plan around with confidence.

<img src="images/monthly_sales_trend.png" alt="Monthly Sales Trend" width="600">

### 6. What actually connects to profit
Looking at how all the key numbers relate to each other, discount is the factor most closely tied to lower profit — more so than order size, quantity, or even how much time has passed. This confirms discount control as the single highest-leverage lever available to improve profitability.

<img src="images/correlation_heatmap.png" alt="Correlation Heatmap" width="600">

*(The full notebook contains 25+ additional business-annotated visualizations covering customers, segments, products, regions, and delivery performance.)*

## ✅ Strategic Recommendations

1. **Cap discounts at 20–25%** for standard sales, and require manager approval above 30% — the threshold where 9 in 10 sales lose money.
2. **Launch a pricing review of Furniture, starting with Tables**, the only product line currently losing money.
3. **Protect and grow the U.S. market** while learning from China and India's more profit-efficient pricing approach.
4. **Plan inventory and staffing around the confirmed Q4 sales peak**, and use the January–February lull for maintenance or off-season promotions.
5. **Set up a recurring review of loss-making products** — about 1 in 6 products in the catalog are currently unprofitable.
6. **Always validate profit metrics with more than one calculation method** — this analysis caught a single bad data row silently breaking an entire category's average.

*(Full detail, evidence, and reasoning for every recommendation is in the notebook and report.)*

## 📁 Repository Structure

```
superstore-sales-performance-analysis/
│
├── README.md                          <- You are here
├── requirements.txt                   <- Python dependencies
|
│
├── data/
│   └── superstore.csv                 <- Raw transactional dataset
│
├── notebooks/
│   └── Superstore_Sales_Performance_Analysis.ipynb   <- Full analysis notebook
│
├── reports/
│   └── Superstore_Sales_Performance_Analysis.html    <- Standalone HTML report (no Jupyter needed)
│
└── images/                            <- Exported chart images used in this README
    ├── discount_vs_profit.png
    ├── profit_by_category.png
    ├── sales_vs_profit_by_subcategory.png
    ├── top10_countries_by_sales.png
    ├── monthly_sales_trend.png
    └── correlation_heatmap.png
```

## 🛠 Tools & Technologies

- **Python 3.10+**
- **Pandas** — data cleaning, aggregation, and analysis
- **NumPy** — numerical computation
- **Matplotlib & Seaborn** — data visualization
- **Jupyter Notebook** — analysis environment and reporting



## 👤 About the Author

**Mutia Kalinda Christian**
Data Analyst | Data Science with AI (in progress) | Kampala, Uganda 🇨🇩🇺🇬

Focused on turning data into clear, actionable business decisions — with a particular interest in data analytics and BI roles. 

- 🔗 LinkedIn: *[https://www.linkedin.com/in/mutia-kalinda-christian-b792063ba/]*
- 📧 Email: *ckchristiankalinda5@gmail.com*



---

<p align="center"><i>If this project was useful or interesting, consider giving it a ⭐ on GitHub!</i></p>
