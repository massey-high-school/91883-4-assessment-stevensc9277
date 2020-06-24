import random

# Create random integer for a, b, c
for item in range(0, 5):
  num_1 = random.randint(0, 10)
  num_2 = random.randint(0, 10)
  num_3 = random.randint(2, 10)
# Display equation but replace 1 with "blank"
  equation = ("{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3))
  print(equation.replace("1", ""))
