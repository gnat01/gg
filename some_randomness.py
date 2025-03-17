import random as random
import numpy ad np
import matplotlib.pyplot as plt # useful for plottin' and schemin'

min_val = 0
max_val = 10

num_gens = 10

random_int_list = []

for i in range(num_gens):
    random_int_list.append(random.randint(min_val, max_val))

print(f"your random list of ints between {min_val} and {max_val} is {random_int_list}")

