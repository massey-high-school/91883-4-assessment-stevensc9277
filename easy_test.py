# Final working quiz
# To do
import random
import math 
from textwrap3 import wrap

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
round_loss = 0
start = 1
text = 'Hello user! Thank you for agreeing to take this test. In this test, you are expected to find the discriminant of an equation generated by the program using the formula: b^2 - 4ac. Enter a number below to start...'

x = wrap(text, 39)
for i in range(len(x)):
    print(x[i])

note = math_statement("! Note: Enter 'h' to display formula  !", "!")

# Get number of questions
max_question = num_check("How many questions do you want to do? ", 10, 50)
while start != max_question + 1:
  num_1 = random.randint(0, 9)
  num_2 = random.randint(0, 9)
  num_3 = random.randint(2, 9)
  rounds = math_statement("* Question {} of {} *".format(start, max_question), "*")
  

  equation = "{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3)
  print(equation.replace("1", ""))
  dis = math.pow(num_2, 2) - 4 * (num_1 * num_3)  

  response = input("Is the discriminant < 0, > 0 or = 0: ").lower()
  if response == ">" and dis == 0 or response == "<" and dis == 0:
    print("Discriminant was = 0")
    print()
    incorrect += 1
    wrong_list.append(equation)
  elif response == ">" and dis < 0 or response == "=" and dis < 0:
    print("Discriminant was < 0")
    print()
    incorrect += 1
    wrong_list.append(equation)
  elif response == "<" and dis > 0 or response == "=" and dis > 0:
    print("Discriminant was > 0")
    print()
    incorrect += 1
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
  elif response == "h":
    print("The formula is: b^2 - 4ac")
    start -= 1
  else:
    print("Please enter either '<', '>' or '='")
    start -= 1
  start += 1
print()
correct = max_question - incorrect
print("You got these incorrect:")
# Print incorrect questions
for item in wrong_list:
  print(item)
  print("You scored {:.0f}%".format(correct/max_question * 100))
