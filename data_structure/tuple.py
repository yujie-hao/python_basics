"""
Tuple is similar to a list

Tuple: element is immutable
list: element is mutable

"""

tuple_1 = ()
print(tuple_1)

tuple_1 = (1, 2,
           3)  # multi-line statement

print(tuple_1)

tuple_1 = ("string1", bool, 1.23, ['a', 1], ('b', 2))
print(tuple_1)

tuple_1 = [1, 'a'], 3.14, False, tuple_1
print(tuple_1)

print(tuple_1[0][1])
print(tuple_1[-1][-2])
print(tuple_1[-1][-2][1])
print(tuple_1[-4])  # print(tuple_1[-5]) and print(tuple_1[4]) are index out of range

# compare
list_1 = [1, 2, 3]
list_1[1] = 10
print(list_1)

tuple_1 = (1, 2, 3, 4)
print(tuple_1)
# tuple_1[1] = 10  # TypeError: tuple object does not support item assignment
print(tuple_1[1])
