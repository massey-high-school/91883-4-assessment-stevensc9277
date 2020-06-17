import random

for item in range(0, 5):
  num_1 = random.randint(0, 10)
  num_2 = random.randint(0, 10)
  num_3 = random.randint(0, 10)
  
  equation = "{}x^2 + {}x + {} = 0".format(num_1, num_2, num_3)
  print(equation.replace("1", "", num_2))
  