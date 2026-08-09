# Data Quality Report — Global Superstore Dataset
*Full audit performed before building the Global Sales Analysis dashboard*

---

## 1. Understanding the Dataset

51,290 rows, 27 columns, covering 2011–2014. Each row represents one product line within an order (one `Order.ID` can contain several rows, one per `Product.ID`). The dataset spans 7 markets (`Market`) split across 13 regions (`Region`), with separate customer (`Customer.ID`) and product (`Product.ID`) reference fields.

**Key structure**: `Row.ID` is the technical unique key for each row. `Order.ID` + `Product.ID` should, in theory, uniquely identify an order line — and that's exactly where the first anomalies surfaced.

---

## 2. Anomalies Detected

### 🔴 Critical — Product.ID ↔ Product.Name inconsistency
**457 `Product.ID` values are linked to more than one product name**, affecting **4,392 rows (8.6% of the dataset)**. Example: `FUR-BO-10000087` maps to both "Dania Classic Bookcase, Mobile" and "Sauder Corner Shelving, Pine" — two completely different pieces of furniture under the same identifier.

*Why it matters*: any dashboard visual ranking "top products" by `Product.Name` would fragment the same physical product across multiple entries, distorting the ranking.

### 🔴 Critical — Geographic misclassification
**97 rows** (Austria: 61, Mongolia: 36) are classified under the **EMEA** market when they don't belong there:
- Austria is a Western European country — all other Austrian rows (270) are correctly classified under **EU market / Central region**.
- Mongolia is an Asian country — the single other Mongolian row is correctly classified under **APAC market / North Asia region**.

*Why it matters*: any map or market-level visual under-counts EU and APAC while over-counting EMEA. This is a well-documented pitfall on this specific "Global Superstore" sample dataset, commonly cited in Power BI/Tableau tutorials.

### 🟠 Moderate — Exact duplicates
**10 fully identical rows** (same order, same product, same quantity, same sales, same profit) — genuine data entry duplicates, not legitimately split order lines.

### 🟠 Moderate — Typographic inconsistencies
**811 rows** in `Product.Name` mix straight quotes (`"`) with typographic/curly quotes (`"` `"`) when expressing inch measurements — an encoding artifact from the original export. This complicates exact text matching and grouping.

### 🟡 Worth monitoring — Extreme discounts
**2,104 rows** carry a discount of 70% or higher, with one extreme case: an order discounted **80%**, dropping sales to 0 with a negative profit — effectively a giveaway. This isn't a data entry error per se (the `Discount` field stays within the valid [0,1] range), but it warrants a business review rather than an automatic correction.

### 🟡 Worth monitoring — Statistical outliers
**7,363 rows (14.4%)** exceed standard statistical bounds (3×IQR) on Sales, Profit, or Shipping Cost. On closer inspection, these are mostly legitimate large B2B orders (e.g., a Canon copier sold for $17,500) — **not errors**, but they can skew averages if not isolated in certain visuals.

---

## 3. What's Clean (good to know)

To avoid over-correcting, here's what was checked and found to be **free of anomalies**:
- No missing values across all 27 columns
- `Discount` is always within the valid [0, 1] range
- No negative or zero `Quantity`
- No negative `Shipping.Cost`
- No shipping date earlier than the order date
- No abnormal delivery delays (>30 days)
- The `Year` column matches the `Order.Date` year on 100% of rows
- `Customer.ID` always maps to a single `Customer.Name` (reliable customer reference)
- No casing variants in country names (`Country`)

---

## 4. Cleaning Actions Performed

| # | Action | Impact |
|---|---|---|
| 1 | Dropped `记录数` (always = 1, no value) and `weeknum` (noise) columns | 2 fewer columns |
| 2 | Removed exact duplicate rows | 10 rows removed |
| 3 | Reclassified Austria: EMEA → EU / Central | 61 rows corrected |
| 4 | Reclassified Mongolia: EMEA → APAC / North Asia | 36 rows corrected |
| 5 | Standardized typographic quotes in `Product.Name` | 43 rows corrected |
| 6 | Harmonized `Product.ID` → canonical name (most frequent) | 1,547 rows corrected |
| 7 | Added `Flag_Extreme_Discount` (discount ≥ 70%) | 2,104 rows flagged, not removed |
| 8 | Added `Flag_Outlier_Value` (statistical outliers) | 7,363 rows flagged, not removed |

**Result: 51,290 → 51,280 rows.** Only genuine duplicates were removed. Extreme values and heavy discounts are **kept but flagged**, so they can be included or excluded from any visual with a simple filter, without losing business information.

The cleaned file (`data/processed/Global_Superstore_Cleaned.csv`) and the Python script that produced it (`scripts/clean_superstore.py`, fully reproducible and documented) are provided for complete traceability.

---

## 5. Recommendations Going Forward

1. **Rebuild the dashboard from `Global_Superstore_Cleaned.csv`**, not the raw file — otherwise market-level visuals (Austria/Mongolia) and product rankings remain distorted.
2. **Add an optional "Exclude extreme discounts" slicer** based on `Flag_Extreme_Discount` on the Profitability page, to demonstrate discount impact on margin transparently.
3. **Use `Flag_Outlier_Value` as an optional filter only**, never as a deletion criterion — these are legitimate B2B sales; removing them would distort the total.
4. **Document this audit in the portfolio.** This kind of work (referential integrity, geographic error detection, duplicate handling, business flags instead of blind deletion) is exactly what separates a "pretty" dashboard from a "trustworthy" one — a strong talking point in interviews.
