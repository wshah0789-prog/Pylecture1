item = input("Enter item name :")
customer = input("Enter your name :")
day = "wed"

if item == "pizza":
    price = 1599
elif item == "burger":
    price = 399
elif item == "wings":
    price = 649
elif item == "fries":
    price = "500"
else:
    price = "item not found"
    exit()
discount_price = price

if customer == "waseem":
    price = 0
    print("free forU sweetie!")
else:
    print("price :", price)

    if day == "wed":
        discount= discount_price * 0.2
        price = discount_price - discount
    else:
        discount = 0
    
    print("discount_price :", price)
    print(f"item :{item}")
    print(f"customer : {customer}")



