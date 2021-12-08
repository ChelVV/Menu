print("Menu")
print("1 – Hamburger – P50.00") 
print("2 – Bacon, egg and Cheese Sandwich - P61.00")
print("3 – Fried Chicken  – P105.00") 
print("4 – Burger Steak  – P88.00")
order1=0
order2=0
order3=0
order4=0
while True:
    order=int(input("Enter your order:"))
    if order == 1:
        m1 = 50
        pcs= int(input("How many Hamburger?"))
        order1= m1 * pcs
        print(order1)
    elif order == 2:
        m2 = 61
        pcs= int(input("How many Bacon, egg and Cheese Sandwich?"))
        order2= m2 * pcs
        print(order2)
    elif order == 3:
        m3 = 105
        pcs= int(input("How many Fried Chicken?"))
        order3= m3 * pcs
        print(order3)
    elif order == 4:
        m4 = 88
        pcs= int(input("How many Burger Steak?"))
        order4= m4 * pcs
        print(order4)
    elif order == 0:
        total = order1 + order2 + order3 + order4
        print("Total amount: ", total)
        pay=int(input("Enter amount:"))
        if pay == total:
            print("You given me the exact amount")
        elif pay >= total:
            change = pay - total
            print("Your change is ", change)
        elif pay <= total:
            print("Your money is not enough")
            chance=int(input("Enter the correct amount again:"))
            if chance == total:
                print("You given me the exact amount")
            elif chance <= total:
                print("Order invalid")
            else:
                change = chance - total
                print("Your change is ", change)
        break
    else:
        print("Invalid order")
    
    




 