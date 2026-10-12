price = float(input("Enter price: "))
discount = int(input("Enter discount %: "))
price_with_discount = round(price - (price * discount/100), 2)

print(f"Price with discount: {price_with_discount}")
print(f"Reduction: {round(price - price_with_discount, 2)}")