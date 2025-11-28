import pandas as pd
import json
from pandasql import sqldf

# Load the JSON file and extract the products array
with open("product-data/ariseism_products.json", 'r') as f:
    data = json.load(f)
    products = data['products']

result = []

for product in products:
    title = product.get('title', '')
    product_type = product.get('product_type', '')
    variants = product.get('variants', [])
    
    if not variants:
        continue
    
    # Extract all unique prices from variants
    prices = set()
    for variant in variants:
        price = variant.get('price')
        if price:
            prices.add(price)
    
    # Check if all variants have the same price
    if len(prices) == 1:
        # Same price across all variants - create 1 row for the product
        result.append({
            'item': title,
            'price': list(prices)[0],
            'product_type': product_type,
        })
    else:
        # Different prices across variants - create 1 row per variant
        for variant in variants:
            variant_title = variant.get('title', '')
            variant_price = variant.get('price')
            
            if variant_price:
                result.append({
                    'item': f"{title} - {variant_title}",
                    'price': variant_price,
                    'product_type': product_type,
                })

# Create DataFrame
df = pd.DataFrame(result)

print(df.head(10))

#print(f"\nProduct types:")
#print(df['product_type'].value_counts())

#print(f"\nPrice statistics:")
#df['price_numeric'] = pd.to_numeric(df['price'], errors='coerce')
#print(df['price_numeric'].describe())

smalltops = """
            SELECT item AS name, product_type AS type, price
            FROM df
            WHERE product_type LIKE '%T-shirt%'
            OR product_type LIKE '%Tanks%'
            """
smalltops_result = sqldf(smalltops, locals())
smalltops_result.to_csv('ariseism_smalltops.csv', index = False)

bigtops = """
            SELECT item AS name, product_type AS type, price
            FROM df
            WHERE product_type LIKE '%Long Sleeves%'
            OR product_type LIKE '%Jacket%'
            """
bigtops_result = sqldf(bigtops, locals())
bigtops_result.to_csv('ariseism_bigtops.csv', index = False)

smallbottoms = """
            SELECT item AS name, product_type AS type, price
            FROM df
            WHERE product_type LIKE '%Skirts%'
            """
smallbottoms_result = sqldf(smallbottoms, locals())
smallbottoms_result.to_csv('ariseism_smallbottoms.csv', index = False)

bigbottoms = """
            SELECT item AS name, product_type AS type, price
            FROM df
            WHERE product_type LIKE '%Pants%'
            OR product_type LIKE '%Bib Overall%'
            """
bigbottoms_result = sqldf(bigbottoms, locals())
bigbottoms_result.to_csv('ariseism_bigbottoms.csv', index = False)

#print(bigbottoms_result.head())

