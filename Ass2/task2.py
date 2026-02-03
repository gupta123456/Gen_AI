def calculate(order_amount):
    if order_amount >= 2000:
        discount = 10
        final_amount = order_amount * 0.9
    else :
        discount = 0
        final_amount = order_amount
    return discount,final_amount

orders = [1200,2500,800,1750,3000]
print("order_amount -> discount& -> final_amount")
for x in orders:
   discount_percent,final_amount = calculate(x)
   print(f"{x} -> {discount_percent} -> {final_amount}")