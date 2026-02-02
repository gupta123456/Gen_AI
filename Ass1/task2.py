categories = ["electronics","apparel","home_decor","electronics","apparel","electronics"]
categories_set = set(categories)
categories_set.add("footwear")
categories_set.add("apparel")
print(categories_set)
check_category = "apparel"
check_exist = check_category in categories_set
print(check_exist)
print(len(categories_set))