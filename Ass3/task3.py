add_gst =  lambda price: price * 1.18
final_price = lambda price, discount_percent: price * 1.18 * (1 - discount_percent / 100)
print(add_gst(100))
print(final_price(1000, 10))