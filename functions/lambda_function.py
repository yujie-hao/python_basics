"""
lambda function: Anonymous function --> function without a name
https://www.programiz.com/python-programming/anonymous-function
"""
nums = [0, 1, 2, 3, 4, 5, 6, 7]

new_list = list(filter(lambda x: (x % 2 == 0), nums))

print(new_list)
