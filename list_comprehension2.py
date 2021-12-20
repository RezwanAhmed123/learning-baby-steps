import random

list_a = random.sample((range(80)), 10)
list_b = random.sample((range(80)), 10)

common_list = {i for i in set(list_a) for j in set(list_b) if i == j}

if len(common_list) == 0:
    print('There are no common elements')
else:
    print(common_list)
