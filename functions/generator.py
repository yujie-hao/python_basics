"""
https://www.programiz.com/python-programming/generator
a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

Note:
1. Once the function yields, the function is paused and the control is transferred to the caller.
2. Local variables and their states are remembered between successive calls.
3. Finally, when the function terminates, StopIteration is raised automatically on further calls.

Advantage:
1. Easy to Implement: Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
2. Memory Efficient
3. Represent Infinite Stream
4. Pipelining Generators

"""


def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 3
    print('This is printed second')
    yield n

    n += 7
    print('This is printed at last')
    yield n


a = my_gen()  # returns an object but does not start execution immediately
print(a)
next(a)
print(a)
next(a)
print(a)
next(a)
print(a)

for item in my_gen():
    print(item)


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x


print(list(fibonacci_numbers(10)))
