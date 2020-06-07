# Program calculates discriminant of a quadratic equation
# To do
import math

# Get user input
num_1 = int(input("Enter a number to assume 'a': "))

num_2 = int(input("Enter another number to assume 'b': "))

num_3 = int(input("Enter your last number to assume 'c': "))

# Calculate discrim...
discriminant = math.pow(num_2, 2) - (4 * num_1 * num_3)

# Ask user if discriminant is greater than, less than or equal to zero
print(discriminant)
question = input("Is the discriminant less than, greater than or equal to zero? ")
