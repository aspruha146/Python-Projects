#Resturant Order's
#menu of the resturant
menu = {
    "burgur": 60,
    "pasta": 80,
    "momos":30,
    "pizza":120,
    "green salad":30,  
    }
#wellcome text
print("wellcome to our resturant")
print("burgur: Rs 60\npasta :Rs 80\nmomos: Rs 30\npizza: Rs120\ngreen salad:30\n ")

total_order=0
item1=input("enter the name of item you want ")
if item1 in menu:
    total_order += menu[item1]
    print(f"your item {item1} has been added to your order ")
else:
    print(f"your item {item1}has not been available yet!")

another_order=input("if you want another order? (yes/no)")
if another_order == "yes":
    item2=input("enter the name of the second item =")
    if item2 in menu:
        total_order += menu[item2]
        print(f"your item {item2} added to your order")
    else:
        print(f"your item {item2}has not been available yet!")
print(f"total amount of your order is{total_order}")
        

    