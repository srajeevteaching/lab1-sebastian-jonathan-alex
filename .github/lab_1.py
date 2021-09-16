# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr.Rajeev
# Date: September 16th, 2021
# Lab Number: Lab 1
# Program Inputs: Input an Integer as ML
# Program Outputs: Output the previous user input converted to Tablespoons and Teaspoons

# Asks for user input in ml
ml = float(input("Enter ml: "))


# Conversions
tablespoons = ml / 15
teaspoons = ml / 5

# Output Converted Inputed
print("Tablespoons: " + str(tablespoons))
print("Teaspoons: " + str(teaspoons))
