#This script is to play with user inputs and type conversions

print("Enter an integer:")
math =  input()

try:
    mathInt = int(math)
except:
    print("That is not an integer, please try again!")
    math = input()

print(mathInt)


