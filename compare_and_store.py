# Stores incorrect question and answer in list then print at end of quiz
# To do
import random
import math 

# Answer checker / comparing check
def ans_check():
  response = input("Is the discriminant < 0, > 0 or = 0: ")
  if response == ">" and dis == 0 or response == "<" and dis == 0:
    print("Discriminant was = 0")
    print()
    wrong_list.append(equation)
  elif response == ">" and dis < 0 or response == "=" and dis < 0:
    print("Discriminant was < 0")
    print()
    wrong_list.append(equation)
  elif response == "<" and dis > 0 or response == "=" and dis > 0:
    print("Discriminant was > 0")
    print()
    wrong_list.append(equation)
  
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
    print("That will not be counted")
    max_question += 1

incorrect = 0
wrong_list = []
max_question = 2
for item in range(0, max_question):
  num_1 = random.randint(0, 9)
  num_2 = random.randint(0, 9)
  num_3 = random.randint(2, 9)
  equation = "{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3)
  print(equation.replace("1", ""))
  dis = math.pow(num_2, 2) - 4 * (num_1 * num_3)  
  answer = ans_check()
  print("The discriminant was {:.0f}".format(dis))
  print()

print("You got these incorrect:")

# Print incorrect questions
for item in wrong_list:
  print(item)