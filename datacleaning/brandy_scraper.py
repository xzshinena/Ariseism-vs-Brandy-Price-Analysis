import requests
import pandas as pd
#time is a built-in python library
#sleep is a function that puts delays inbetween requests so that we seeem human since some webs block too many requests at once
from time import sleep
from pandasql import sqldf

def get_prods(max_pages = 5):
    #this function is the scraper for brandy's web products
    all_products = []
    base_url = "https://us.brandymelville.com/collections/all/products.json"
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}&limit=250"
        response = requests.get(url)

        data = response.json()
        products = data.get('products',[])

        for product in products:
            if product['variants']:
                variant = product['variants'][0]
            else:
                variant = {}
            
            all_products.append({
                'name' : product['title'],
                'type' : product['product_type'],
                'price' : variant.get('price','N/A')
            })

        sleep(1)

    df = pd.DataFrame(all_products)
    return df

df = get_prods(max_pages = 10)
#print(df.head())

types = []
for item_type in df['type']:
    if item_type not in types :
        types.append(item_type)
#for item_type in types :
    #print(item_type)

smalltops = """
            SELECT name, type, price
            FROM df
            WHERE type LIKE '%Tanks%'
            or type LIKE '%Tank%'
            or type LIKE '%T-Shirts%'
            or type LIKE '%Shirts%'
            """
smalltops_result = sqldf(smalltops, locals())
smalltops_result.to_csv('data-viz/brandy_smalltops.csv', index = False)

bigtops = """
        SELECT name, type, price
            FROM df
            WHERE type LIKE '%Sweaters%'
            or type LIKE '%Hoodies%'
            or type LIKE '%Sweatshirts%'
            or type LIKE '%Long Sleeve%'
        """
bigtops_result = sqldf(bigtops, locals())
bigtops_result.to_csv('data-viz/brandy_bigtops.csv', index = False)

bigbottoms = """
            SELECT name, type, price
            FROM df
            WHERE type LIKE '%Sweatpants%'
            or type LIKE '%Pants%'
            or type LIKE '%Jeans%'
            """
bigbottoms_result = sqldf(bigbottoms, locals())
bigbottoms_result.to_csv('data-viz/brandy_bigbottoms.csv', index = False)

smallbottoms = """
            SELECT name, type, price
            FROM df
            WHERE type LIKE '%Skirts%'
            or type LIKE '%Shorts%'
            """
smallbottoms_result = sqldf(smallbottoms, locals())
smallbottoms_result.to_csv('data-viz/brandy_smallbottoms.csv', index = False)

