# Create function to check discriminant answer and ompare with user
# I have good naming sense
import random
import math

# Function to check and compare discriminant with user input (Best so far)
def ans_check(question, equal, lower, higher):
  error = "That is incorrect"
  while True:
      try:
        response = input("What is the discriminant? ")
        if response in equal and dis == 0:
          print("Correct!")
          print()
          return response
        elif response in lower and dis < 0:
          print("Correct!")
          print()
          return response
        elif response in higher and dis > 0:
          print("Correct!")
          print()
          return response
        else:
          print(error)
      except ValueError:
        print(error)
      

for item in range(0, 5):
  equal = ["=", "equal", "e"]
  lower = ["<", "lower", "l"]
  higher = [">", "higher", "h"]
  num_1 = random.randint(1, 9)
  num_2 = random.randint(1, 9)
  num_3 = random.randint(2, 9)
  dis = math.pow(num_2, 2) - (4*num_1*num_3)
  print()
  equation = "{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3)
  print(equation.replace("1", ""))
  question = ans_check("", equal, lower, higher)
  print("{:.0f}".format(dis))