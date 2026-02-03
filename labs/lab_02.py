# Prompt the user to input 2 numbers to do operations on
left_side = float(input("Please enter your first number: "))
right_side = float(input("Please enter your second number: "))

# Define variables for the results of each operation
left_right_add = left_side + right_side
left_right_subtract = left_side - right_side
left_right_multiply = left_side * right_side
left_right_exponent = left_side ** right_side
left_right_divide = left_side / right_side
left_right_floor = left_side // right_side
left_right_mod = left_side % right_side

# Display the result of each of the 7 operations
print(f"\nResults:\nAddition: {left_right_add}\nSubtraction: {left_right_subtract}\nMultiplication: {left_right_multiply}\nExponentiation: {left_right_exponent}\nDivision: {left_right_divide}\nFloor division: {left_right_floor}\nModulus: {left_right_mod}")
