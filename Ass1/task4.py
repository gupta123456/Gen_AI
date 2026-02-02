catlog = [("laptop",12000,"electronics"),("shirt","1000","apparel"),("pen",20,"stationary"),("soap","30","daily"),("tv",20000,"electronics")]
category_to_products = {}
for product_name,price,category in catlog:
    if category not in category_to_products:
        category_to_products[category]=product_name
        
print(category_to_products)
max_products = max(category_to_products,key=lambda k:len(category_to_products))
print(max_products)