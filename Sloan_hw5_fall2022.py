# Create Header Variable

header = ("* Welcome! This is homework 5 for Sebastian Sloan Due 10/13/2022*")

print(header)

print("")
print("")

# Instructions

print("Below you will be asked to input any 5 numbers of your choosing")
print("Please input each number one at a time, then the program will total and average of")
print("your numbers for you, Thank you!")

print("")
print("*PLEASE NOTE!: numbers entered will only be counted")
print("to the second decimal place.")

print("")
print("")
print("")
print("")

# Create Inputs

firstNum = input("Please input any number:")

print(round(float(firstNum),2))
print("")

secondNum = input("Please input any number:")

print(round(float(secondNum),2))
print("")

thirdNum = input("Please input any number:")

print(round(float(thirdNum),2))
print("")

fourthNum = input("Please input any number:")

print(round(float(fourthNum),2))
print("")

fithNum = input("Please input any number:")

print(round(float(fithNum),2))
print("")

# Total numbers together

numberInputs = [round(float(firstNum),2), round(float(secondNum),2), round(float(thirdNum),2), round(float(fourthNum),2), round(float(fithNum),2)]

totalOfNumbers = round(sum(numberInputs),2)

print("")
print("")
print("")

print("Thank you,")
print(f"the values you entered are: {round(float(firstNum),2)}, {round(float(secondNum),2)}, {round(float(thirdNum),2)}, {round(float(fourthNum),2)} and {round(float(fithNum),2)}")
print(f"the total of the numbers you input is: {totalOfNumbers}")
print(f"the average of your input numbers is: {round(float(totalOfNumbers/5),2)}")
