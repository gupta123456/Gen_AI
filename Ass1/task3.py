price_dict = {"brush":50,"soap":30,"paint":200,"pen":20,"oil":10,"water":20}
price_dict["fridge"]=10000
print(price_dict)
price_dict["oil"]=20
print(price_dict)
product_remove = "brush"
if product_remove in price_dict:
    del price_dict[product_remove]
else:
    print("Product does not exist")
print(price_dict)
total_sum = sum(price_dict.values())
total = len(price_dict)
print(total_sum/total)