#item = int(input("Tell me your price: "))

# item_type = type(item)

# print(item_type)


#tip_amount = item * 0.2

#total_amount = item + tip_amount

#print(f"Your tip amount is: {tip_amount}")

#print(f"Your total amount is {total_amount}")

list = input("enter item name :")
name = input("enter your name ")


if list == "burger":
    price= 400
elif list == "wings":
    price = 300
else:
    price = "not found"
    exit()

if name == "Memoona":
    price = 0
    print("free for you sweetie")
    discount = 0

    discount = price * 0.4

total_price = price - discount
print(f"price : {price}")
print(f"discount : {discount}")
print(f"total price : {total_price}")
