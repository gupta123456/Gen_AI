daily = [200,150,0,400,50,-1,300]
total_sales = 0

for day_sales in daily:
    if day_sales == -1:
        print("Corrupted data")
        break
    elif day_sales == 0:
        print("Day with no sales. Skipping")
        continue
    else:
        total_sales += day_sales
        print(f"Added {day_sales} to total")
print(f"The final total : ${total_sales}")