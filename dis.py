# Program calculates discriminant of a quadratic equation
# To do
import math


# Number checker
def num_check(question, low=None, high=None):
    # sets up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))
            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# Get user input
num_1 = num_check("Enter a number to assume 'a': ")

num_2 = num_check("Enter another number to assume 'b': ")

num_3 = num_check("Enter your last number to assume 'c': ")

# Calculate discrim...
discriminant = math.pow(num_2, 2) - (4 * num_1 * num_3)

# Ask user if discriminant is greater than, less than or equal to zero
question = input("Is the discriminant less than, greater than or equal to zero? ")
if question == "<" and discriminant < 0:
  print("Correct")

elif question == ">" or question == "=" and discriminant < 0:
  print("Wrong. Try again")

elif question == ">" and discriminant > 0:
  print("Correct")

elif question == "<" or question == "=" and discriminant > 0:
  print("Wrong. Try again")

elif question == "=" and discriminant == 0:
  print("Correct")

elif question == "<" or question == ">" and discriminant == 0:
  print("Wrong. Try again")

print("The discriminant was {:.2f}".format(discriminant))
