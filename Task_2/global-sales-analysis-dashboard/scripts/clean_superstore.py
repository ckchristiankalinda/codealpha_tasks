"""
Global Superstore — Data Cleaning Pipeline
Fixes referential integrity, geographic misclassification, duplicates,
and text encoding issues found during the data quality audit.
See docs/Data_Quality_Report.md for full rationale behind each step.
"""

import pandas as pd
import re

df = pd.read_csv('../data/raw/superstore.csv')  # adjust path if running standalone
original_rows = len(df)
log = []

# 1. Drop noise columns
cols_to_drop = ['记录数', 'weeknum']
df = df.drop(columns=cols_to_drop)
log.append(f"Dropped noise/unused columns: {cols_to_drop}")

# 2. Remove exact duplicate order lines
before = len(df)
df = df.drop_duplicates(subset=['Order.ID', 'Product.ID', 'Quantity', 'Sales', 'Profit'], keep='first')
removed_dup = before - len(df)
log.append(f"Removed exact duplicate rows: {removed_dup}")

# 3. Fix Austria / Mongolia geographic misclassification
mask_austria = (df['Country'] == 'Austria') & (df['Market'] == 'EMEA')
mask_mongolia = (df['Country'] == 'Mongolia') & (df['Market'] == 'EMEA')
n_austria = mask_austria.sum()
n_mongolia = mask_mongolia.sum()
df.loc[mask_austria, 'Market'] = 'EU'
df.loc[mask_austria, 'Region'] = 'Central'
df.loc[mask_mongolia, 'Market'] = 'APAC'
df.loc[mask_mongolia, 'Region'] = 'North Asia'
log.append(f"Reclassified Austria EMEA -> EU/Central: {n_austria} rows")
log.append(f"Reclassified Mongolia EMEA -> APAC/North Asia: {n_mongolia} rows")

# 4. Standardize typographic quotes in Product.Name
def normalize_quotes(s):
    if not isinstance(s, str):
        return s
    return re.sub(r'[\u201c\u201d\u2033]', '"', s)

before_sample = df['Product.Name'].copy()
df['Product.Name'] = df['Product.Name'].apply(normalize_quotes)
n_quotes_fixed = (before_sample != df['Product.Name']).sum()
log.append(f"Standardized typographic quotes in Product.Name: {n_quotes_fixed} rows")

# 5. Harmonize Product.ID -> Product.Name (canonical name = most frequent per ID)
canonical_names = df.groupby('Product.ID')['Product.Name'].agg(lambda x: x.value_counts().idxmax())
before_names = df['Product.Name'].copy()
df['Product.Name'] = df['Product.ID'].map(canonical_names)
n_names_fixed = (before_names != df['Product.Name']).sum()
log.append(f"Harmonized product names to canonical name per Product.ID: {n_names_fixed} rows changed")

# 6. Flag extreme discount orders (>=70%) for business review
df['Flag_Extreme_Discount'] = df['Discount'] >= 0.7
log.append(f"Flagged extreme discount orders (>=70%): {df['Flag_Extreme_Discount'].sum()}")

# 7. Flag statistical outliers on Sales/Profit/Shipping Cost, without removing them
def iqr_flag(series, k=3):
    Q1, Q3 = series.quantile([.25, .75])
    IQR = Q3 - Q1
    return (series < Q1 - k * IQR) | (series > Q3 + k * IQR)

df['Flag_Outlier_Value'] = iqr_flag(df['Sales']) | iqr_flag(df['Profit']) | iqr_flag(df['Shipping.Cost'])
log.append(f"Flagged statistical outlier rows (likely legitimate large B2B orders): {df['Flag_Outlier_Value'].sum()}")

df.to_csv('../data/processed/Global_Superstore_Cleaned.csv', index=False)

print(f"Rows before: {original_rows} | after: {len(df)}")
print("\n".join(log))
