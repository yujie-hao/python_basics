"""
lambda function: Anonymous function --> function without a name
https://www.programiz.com/python-programming/anonymous-function
"""

print("=== lambda function ===")
nums = [0, 1, 2, 3, 4, 5, 6, 7]

new_list = list(filter(lambda x: (x % 2 == 0), nums))

print(new_list)

double = lambda x: x * 2  # double is not the function name, but a reference to the lambda function
print(double(5))

double = lambda x: x * 2.1
print(double(5))

my_list = [1, 5, 11, 4, 8, 11, 17, 0]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)
new_list = filter(lambda x: (x % 2 == 0), my_list)
print(new_list)  # not a list

print("=== map function ===")
my_list = [1, 5, 4, 6, 8, 11, 18, 2, 6]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)
new_list = map(lambda x: x * 2, my_list)
print(new_list)  # not a list
