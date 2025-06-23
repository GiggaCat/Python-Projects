dict1 = {"Burger" : 50,"Pizza":100,"Coffee":150,"Sandwhich":80,"Momos":60,"Chowmien":100,"Coca-cola":40,"Fries":70}
print(dict1)
bill = 0
for i in dict1:
    your_food = input("What would you like to have: ")
    if (your_food in dict1):
        bill += dict1[your_food]
        print(f"Your order {your_food} is placed")
        break
    else:
        print(f"Sorry but currently {your_food} is not available")
        break

for i in dict1:
    your_food2 = input("Would you like something else: ")
    if (your_food2 in dict1):
        bill += dict1[your_food2]
        print(f"Great!!Your past order and {your_food2} will be ready soon")
        print(f"Your total bill is {bill}")
    elif (your_food2 == "No"):
        print(f"Thank you!! Your order will be ready soon...")
        print(f"Your Bill is {bill}")
        break
    else:
        print(f"Thank you!! Your order will be ready soon...")
        print(f"Your Bill is {bill}")
        break
