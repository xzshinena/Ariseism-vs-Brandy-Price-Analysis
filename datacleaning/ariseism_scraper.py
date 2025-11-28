import pandas as pd
from pandasql import sqldf
import json

products = pd.read_json("/Users/shinena/dev/Taobao-vs-Western-Fashion-Brands/ariseism_products.json")
with open("/Users/shinena/dev/Taobao-vs-Western-Fashion-Brands/ariseism_products.json", 'r') as f:
    data = json.load(f)

ariseism_products = pd.DataFrame(data['products'])

ariseism_products['price'] = ariseism_products['variants'].apply(
    lambda x : x[0]['price'] if x and len(x) > 0 else None
)

ariseism_products['tags_str'] = ariseism_products['tags'].apply(
    lambda x : ','.join(x) if x else ''
)

items = """
        SELECT title, product_type AS type, tags_str AS tags, price
        FROM ariseism_products
        WHERE price IS NOT NULL
        """
items_result = sqldf(items, locals())
print(items_result.head())