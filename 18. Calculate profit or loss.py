cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    print(f"Profit = {selling_price - cost_price}")
elif cost_price > selling_price:
    print(f"Loss = {cost_price - selling_price}")
else:
    print("No profit, no loss")






      




