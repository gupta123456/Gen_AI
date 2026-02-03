orders = []
while True:
    print("\nMenu options:")
    print("1 = Add order amount to a running list")
    print("2 - Show all orders and totals after applying discounts")
    print("q - Quit")
    choice = input("Enter your choice:")

    if choice == 'q':
        break
    elif choice == '1':
        try:
            amount = float(input("Enter order amount : "))
            orders.append(amount)
            print(f"Order of ${amount} added.")
        except ValueError:
            print("Invalid amount.")
            continue
    elif choice == '2':
        if not orders:
            print("No orders to show.")
        else:
            print("All orders : ")
            for order in orders :
                print(f"${order}")
            total = sum(orders)
            discount = total*0.1 if total > 100 else 0
            print(f"Total before discount : ${total}")
            print(f"Discount applied 10% : ${discount}")
            print(f"Total after discount : ${total - discount}")
    else:
        print("Invalid Input.")
        continue