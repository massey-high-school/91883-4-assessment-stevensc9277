# Get necessary modules
import time
import random

# Simple math in a loop
for item in range(0, 5):
  num_1 = random.randint(1, 5) 
  num_2 = random.randint(1, 5)
  multiply = num_1 * num_2    # Quick math
  # Print equations
  print("{} * {} = {}".format(num_1, num_2, multiply))
  time.sleep(2.5)   # Stop program for 2.5 seconds