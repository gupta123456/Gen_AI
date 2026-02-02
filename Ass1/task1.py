products = ["brush","soap","paint","pen","oil","water"]
sample_product = ("brush","100","oral")
print(products[2],products[-1])
products.append("tv")
products.append("machine")
print(products)
new_product = list(sample_product)
new_product[1]=200
sample_product = tuple(new_product)
print(sample_product)