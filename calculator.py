#Alan
#Calculator
#Creates a program that prompts users to enter two numbers, an operator, and prints the result of the operation

#Init
#Functions
def main():
#Welcome Message
    print("Welcome to Basic Calculator!")
#Collect Input
    num1 = int( input("Please enter a number: ") )
    num2 = int( input("Please enter a number: ") )
    operator = input("Please enter an operator (+,-,*,/): ")
#Perform Operation
    if operator == "+":
        print(calc_sum(num1,num2))
    elif operator == "-":
        print(calc_sub(num1,num2))
    elif operator == "*":
        print(calc_mult(num1,num2))
    elif operator == "/":
        print(calc_div(num1,num2))
    else:
        print("An error has occured. Please enter a valid operator and try again.")
#This function adds two numbers and returns the total
def calc_sum(x,y):
    return x+y
def calc_sub(x,y):
    return x-y
def calc_mult(x,y):
    return x*y
def calc_div(x,y):
    return x/y

#Main
main()
