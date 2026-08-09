# Global Sales Analysis — Power BI Build Reference

Reference documentation for how this dashboard was built: data prep, DAX measures, and visuals used across all three pages.

---

## 1. Data Preparation (Power Query)

- Import `data/processed/Global_Superstore_Cleaned.csv`
- Confirm `Flag_Extreme_Discount` and `Flag_Outlier_Value` load as Boolean type
- Set `Order.Date` and `Ship.Date` to Date type
- Build a dedicated `Calendar` table and relate it to `Order.Date` (1-to-many) for time intelligence:
  ```
  Calendar = CALENDAR(DATE(2011,1,1), DATE(2014,12,31))
  Year = YEAR('Calendar'[Date])
  Quarter = QUARTER('Calendar'[Date])
  Month = FORMAT('Calendar'[Date], "MMM")
  ```

---

## 2. DAX Measures

```dax
Total Sales =
SUM(Orders[Sales])

Total Profit =
SUM(Orders[Profit])

Profit Margin % =
DIVIDE([Total Profit], [Total Sales], 0)

Total Orders =
DISTINCTCOUNT(Orders[Order.ID])

Total Customers =
DISTINCTCOUNT(Orders[Customer.ID])

Avg Discount =
AVERAGE(Orders[Discount])

Avg Order Value =
DIVIDE([Total Sales], [Total Orders])

Avg Shipping Cost =
AVERAGE(Orders[Shipping.Cost])

Loss Making Orders % =
DIVIDE(
    CALCULATE(COUNTROWS(Orders), Orders[Profit] < 0),
    COUNTROWS(Orders)
)

YoY Sales Growth % =
VAR CurrentSales = [Total Sales]
VAR PriorSales =
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
RETURN
    DIVIDE(CurrentSales - PriorSales, PriorSales)

Sales % of Total =
DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Orders)))

Profit % of Total =
DIVIDE([Total Profit], CALCULATE([Total Profit], ALL(Orders)))

Sales 2011 =
CALCULATE([Total Sales], 'Calendar'[Year]=2011)

Sales 2014 =
CALCULATE([Total Sales], 'Calendar'[Year]=2014)

Growth 2011-2014 % =
DIVIDE([Sales 2014]-[Sales 2011], [Sales 2011])
```

**Validation benchmarks**: Total Sales = 12,641,151 | Total Profit = 1,467,237 | Profit Margin % = 11.6% | Total Orders = 25,035 | Avg Discount = 14.3%.

---

## 3. Dashboard Pages & Visuals

### Page 1 — Global Sales Overview

| Visual | Fields | Purpose |
|---|---|---|
| Card | Total Sales | Headline KPI |
| Card | Total Profit | Headline KPI |
| Card | Profit Margin % | Headline KPI |
| Card | Total Orders | Headline KPI |
| Card | Avg Discount | Context KPI |
| Filled Map | Location = Country, Size/Color = Total Sales | Global geographic view |
| Line Chart | Axis = Calendar[Year], Values = Total Sales, Total Profit | 2011→2014 trend |
| Clustered Bar Chart | Axis = Category, Value = Total Sales | Category breakdown |
| Treemap | Category = Market, Value = Total Sales | Market weight |
| Clustered Bar Chart | Axis = Market, Value = Growth 2011-2014 % | Market growth comparison |
| Slicer | Calendar[Year] | Time filter |
| Slicer | Market | Geographic filter |

### Page 2 — Profitability & Risk Analysis

| Visual | Fields | Purpose |
|---|---|---|
| Bar Chart (sorted) | Axis = Sub.Category, Value = Total Profit + conditional formatting | Reveals the only loss-making sub-category (Tables) |
| Table | Ship.Mode, Total Sales, Total Profit, Avg Shipping Cost | Shipping mode cost/profit impact |
| Bar Chart (Top N = 5) | Axis = Country, Value = Total Profit | Top loss-making countries |
| Table (Top N = 10) | Customer.Name, Total Sales, Total Profit, Profit Margin % | Top customers by profit |
| Scatter Chart | X = Discount, Y = Profit, Detail = Sub.Category | Discount/profit correlation |
| Card | Loss Making Orders % | Headline risk KPI |
| Slicer | Segment | Customer segment filter |
| Slicer (Between) | Discount | Discount range filter |

### Page 3 — Key Observations & Recommendations

Two text boxes summarizing the analysis in business language: key observations on the left, prioritized recommendations on the right. No additional charts — this page is meant to synthesize, not analyze.

---

## 4. Branding

- Navy `#1B2A4A` — titles, card backgrounds, table headers
- Gold `#A8832A` — positive highlights, key figures, action words
- Red (e.g. `#C0392B`) — reserved for negative values (loss-making sub-categories, countries)
- Font: Segoe UI or Georgia (Cambria is not natively supported in Power BI)
