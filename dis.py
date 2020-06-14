# Program calculates discriminant of a quadratic equation
# To do
import random
import math

# Answer checking function (Must be either >, < or =)
def ans_check():
  response = input("Is the discriminant < 0, > 0 or = 0: ")
  if response == ">" and dis == 0 or response == "<" and dis == 0:
    print("Discriminant was = 0")
    print()
  elif response == ">" and dis < 0 or response == "=" and dis < 0:
    print("Discriminant was < 0")
    print()
  elif response == "<" and dis > 0 or response == "=" and dis > 0:
    print("Discriminant was > 0")
    print()
  elif response == ">" and dis > 0:
    print("That is correct!")
    print()
  elif response == "<" and dis < 0:
    print("That is correct!")
    print()
  elif response == "=" and dis == 0:
    print("That is correct!")
    print()
  else:
    print()

total_score = 5

num_1 = random.randint(0, 10)
num_2 = random.randint(0, 10)
num_3 = random.randint(0, 10)

for item in range(0, 5):
  print("{}x² + {}x + {} = 0".format(num_1, num_2, num_3))

  dis = math.pow(num_2, 2) - 4 * (num_1 * num_3)  
  answer = ans_check()
  print("The discriminant was {:.0f}".format(dis))
  print()
  num_1 = random.randint(0, 10)
  num_2 = random.randint(0, 10)
  num_3 = random.randint(0, 10)

print("You scored {:.2f}% ".format(total_score / 5 * 100))
