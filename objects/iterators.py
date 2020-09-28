"""
https://www.programiz.com/python-programming/iterator
Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.
"""

# iter() function returns an iterator from an iterable object
my_list = [4, 7, 0, 3]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
# print(my_iter.__next__()) #Error: StopIteration

nums = [10, 200, 300, 50]
it = iter(nums)

while True:
    try:
        print(next(it))
    except StopIteration:
        break
