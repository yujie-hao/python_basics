from functools import reduce
my_list = [1, 2, 3, 4]
new_list = reduce(lambda x, y: y ** x, my_list)  # iterative operation
# [1, 2, 3, 4] --> [2, 3, 4] --> [9, 4] --> [262144]
print(my_list)
print(new_list)
