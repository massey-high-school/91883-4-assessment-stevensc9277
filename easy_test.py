# Final working quiz
# To do
# Assemble all components
# Get someone to test program
# Change if needed
import random
import math 
import time   # I thought this would look cool
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

# answer checking function (compare dis and input)
def ans_check(question, equal, lower, higher):
  global incorrect    # Prevents the UnboundLocalError
  error = "That is incorrect"
  display = "Discriminant was {:.0f}".format(dis)
  while True:
      try:
        response = input("What is the discriminant? ").lower()
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
        elif response == "a":
          print("The formula is: b^2 - 4ac")
        else:
          print(error)
          num_list.append(start)
          wrong_list.append(equation)
          answer.append(display)
          incorrect += 1
          print()
          return response
      except ValueError:
        print(error)


equal = ["=", "equal", "e"]   # Used if discriminant is 0
lower = ["<", "lower", "l"]   # Used if discriminant is < 0
higher = [">", "higher", "h"]   # Used if discriminant is > 0
answer = []   # Collect discriminant values
wrong_list = []   # Collect incorrect questions
num_list = []
incorrect = 0
start = 1
# Basic introduction and explanation
text = 'Hello user! Thank you for agreeing to take this test. In this test, you are expected to find the discriminant of an equation generated by the program using the formula: b^2 - 4ac. At any time you may forget the formula, type "a" or "A"...'

# Format paragraphs (improves aesthetics)
x = wrap(text, 39)
for i in range(len(x)):
    print(x[i])

print()
# Get number of questions
max_question = num_check("How many questions do you want to do? ", 5, 50)
# Ask user to get ready (For fun)
print("Generating questions. Please get ready...")
time.sleep(3)
while start != max_question + 1:
  num_1 = random.randint(0, 9)
  num_2 = random.randint(0, 9)
  num_3 = random.randint(2, 9)
  # Display round number and max
  rounds = math_statement("- Question {} of {} -".format(start, max_question), "-")
  # Display question to solve (find discriminant) but replace 1 with blank
  equation = "{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3)
  print(equation.replace("1", ""))
  dis = math.pow(num_2, 2) - 4 * (num_1 * num_3)  
  # Get user input (answer)
  user_input = ans_check("What is the discriminant? ", equal, lower, higher)
  start += 1

# Find number of questions answered correctly
correct = max_question - incorrect
print("Finding incorrect questions. Please wait...")    # I only put this in because I thought it was cool
time.sleep(2.5)
if correct != max_question:
  print("It seems that you got a few questions wrong...")
  time.sleep(2)
  print()
  # Print incorrect questions
  show = zip(num_list, wrong_list, answer)
  for item in show:
    print(*item, sep = " | \t ")
else:
  print("No incorrect questions found...👍")
print()
# Print percentage of questions answered correctly
score = math_statement("* You scored {:.0f}%  *".format(correct/max_question * 100), "*")
print("Thank you for finishing the test. Keep studying o(*^▽ ^*)┛")
