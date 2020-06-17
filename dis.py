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

for item in range(0, 5):
  num_1 = random.randint(0, 10)
  num_2 = random.randint(0, 10)
  num_3 = random.randint(2, 10)
  equation = "{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3)
  print(equation.replace("1", ""))

  dis = math.pow(num_2, 2) - 4 * (num_1 * num_3)  
  answer = ans_check()
  print("The discriminant was {}".format(dis))
  print()

print("You scored {:.0f}% ".format(total_score / 5 * 100))
