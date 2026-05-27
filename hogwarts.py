#Alan
#Hogwarts
#Asks user for their name and then randomly assigns them a Hogwarts house

#Init
import random
import time
#Functions
def main():
    #Welcome Message
    print("Hello, Wizard! Welcome to Hogwarts! Today, we will assign you a house! Sit and answer some questions for the hat!")
    #Obtains name
    name=input("Nice to see you Wizard! Now tell me, what is your name? ")
    name=name.lower()
    print("I like the name, let's give you your house!")
    #Builds suspense fr
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print("Almost there... just wait a few more seconds!")
    time.sleep(3)
    #Randomizes house
    print("You are in " + house(name))
    while True:
        next=input("Would you like to be reassigned? (yes or no) ")
        if next.lower() == "no":
            print("Exiting program...")
            time.sleep(1)
            break
        elif next.lower() == "yes":
            print(f"You entered: {next}")
            main()
        else:
            print("Oops, that wasn't a recognized command! Please only enter yes or no.")
            continue

def house(name):
    if name == "harry" or name == "ron" or name == "hermione":
        return "Gryffindor!"
    elif name == "newt" or name == "nymphadora" or name == "pomona":
        return "Hufflepuff!"
    elif name == "luna" or name == "cho" or name == "filius":
        return "Ravenclaw!"
    elif name == "voldemort" or name == "draco" or name == "severus":
        return "Slytherin!"
    else:
        num = random.randint(1,4)
        #Assigns 1 to Gryffindor
        if num == 1:
            return "Gryffindor!"
        elif num == 2:
            return "Hufflepuff!"
        elif num == 3:
            return "Ravenclaw!"
        elif num == 4:
            return "Slytherin!"
#Main
main()
