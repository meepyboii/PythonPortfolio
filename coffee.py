#Alan
#Coffee
#Asks the customer a few questions about drink preferences and recommends a drink!
def recommendation():
    print("Welcome to Le Cafe!")
    temp=input("Do you want your drink hot or cold?: ")
#Hot Recommendation
    if temp == "hot":
        flavor1=input("Do you want your drink sweet? (yes,no): ")
        if flavor1 == "yes":
            print("You should get a Hot Chocolate")
        elif flavor1 == "no":
            print("You should get a Black Coffee")
#Cold Recommendation
    elif temp == "cold":
        flavor2=input("Do you want your drink sweet? (yes,no): ")
        if flavor2 == "yes":
            print("You should get an Iced Latte")
        else:
            print("You should get a Cold Brew")

recommendation()
