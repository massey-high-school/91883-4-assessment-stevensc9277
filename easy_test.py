# Final working quiz
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

# Statement generator
def math_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()

# Number checker function
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


incorrect = 0
wrong_list = []
start = 1
# Get number of questions
max_question = num_check("How many questions do you want to do? ", 10, 50)
for item in range(0, max_question):
  num_1 = random.randint(0, 9)
  num_2 = random.randint(0, 9)
  num_3 = random.randint(2, 9)
  rounds = math_statement("* Question {} of {} *".format(start, max_question), "*")
  start += 1
  equation = "{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3)
  print(equation.replace("1", ""))
  dis = math.pow(num_2, 2) - 4 * (num_1 * num_3)  
  answer = ans_check()
  print("The discriminant was {:.0f}".format(dis))
  print()

print("You got these incorrect:")

# Print incorrect questions
for item in wrong_list:
  print("Question {}: {}".format(start, item))
