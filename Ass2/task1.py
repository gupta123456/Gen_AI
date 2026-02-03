import sys

def calculate(order_amount):
    if order_amount >= 2000:
        discount = 0.15
    elif 1500 <= order_amount < 2000:
        discount = 0.10
    elif 1000 <= order_amount <1500:
        discount = 0.07
    else :
        discount = 0
    subTotal = order_amount*(1 - discount)
    tax_rate = 0.05
    tax = subTotal * tax_rate
    final = subTotal + tax

    print(f"SubTotal : ${subTotal}")
    print(f"Tax : ${tax}")
    print(f"Final : ${final}")

try:
    order_amount = input("Enter the number : ")
    order_amount = int(order_amount)
    print(order_amount)
    if(order_amount < 0):
        print("Order cannot be negative")
        sys.exit(1)
    calculate(order_amount)
except ValueError:
    print("Invalid Inout")