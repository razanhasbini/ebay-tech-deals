import pandas as pd

df = pd.read_csv('ebay_tech_deals.csv', dtype=str)

def clean_price(p):
    if pd.isna(p):
        return None
    return p.replace('US', '').replace('$', '').replace(',', '').strip()

df['Price'] = df['Price'].apply(clean_price)
df['Original_price'] = df['Original_price'].apply(clean_price)
df['Original_price'] = df['Original_price'].fillna(df['Price'])
df['Shipping'] = df['Shipping'].apply(lambda x: x.strip() if isinstance(x, str) else "")
df['Shipping'] = df['Shipping'].replace(["", "N/A", None], "Shipping info unavailable")
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Original_price'] = pd.to_numeric(df['Original_price'], errors='coerce')
df['discount_percentage'] = ((df['Original_price'] - df['Price']) / df['Original_price'] * 100).round(2)
df['discount_percentage'] = df['discount_percentage'].fillna(0)

df.to_csv('cleaned_ebay_deals.csv', index=False)

print("✅ Cleaned data saved to cleaned_ebay_deals.csv")
