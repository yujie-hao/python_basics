"""
[Python set] is an unordered collection of items.
Every set element is unique and must be immutable (cannot not be changed).
However, a set itself is mutable. We can add or remove items from it
"""

#  creation
print("=== creation ===")
my_set = {1, 2, 3, 2, 1}
print(my_set)

my_set = {1.0, "Hello", (1, 2, 3), "Hello", (1, 2, 3)}
print(my_set)

list_1 = [1, 2, 1]
print(list_1)
my_set = set(list_1)
print(my_set)

tuple_1 = (1, 2, 1)
print(tuple_1)
my_set = set(tuple_1)
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.
# my_set = {1, 2, [3, 4]}
# print(my_set) # TypeError: unhashable type: 'list'

my_set = {1, 2, (3, 4)}
print(my_set)  # tuple is immutable

# this makes a dictionary, not set
a = {}
print(type(a))

a = set()
print(type(a))

print("=== update ===")
my_set = {1, 3}
my_set.add(2)
print(my_set)

my_set.update([12, 10, 11])
print(my_set)

print("=== remove ===")
my_set.remove(2)
# my_set.remove(20)  # remove: element needs to be in set, otherwise: KeyError: 20
print(my_set)
my_set.discard(10)  # discard: element doesn't need to be in set
print(my_set)

print(my_set.pop())
print(my_set.pop())
print(my_set)

my_set.clear()
print(my_set)

print("=== operation ===")
set_A = {1, 2, 3}
set_B = {4, 2, 5}
print("set union:")
print("set_A | set_B: ", set_A | set_B)
print("set_A.union(set_B): ", set_A.union(set_B))
print("set_B.union(set_A): ", set_B.union(set_A))

print("---\nset intersection")
print("set_A & set_B: ", set_A & set_B)
print("set_A.intersection(set_B)", set_A.intersection(set_B))
print("set_B.intersection(set_A)", set_B.intersection(set_A))

print("---\nset difference")
print("set_A - set_B: ", set_A - set_B)
print("set_A.difference(set_B): ", set_A.difference(set_B))
print("set_B - set_A: ", set_B - set_A)
print("set_B.difference(set_A): ", set_B.difference(set_A))

print("---\nset symmetric difference")
print("set_A ^ set_B: ", set_A ^ set_B)
print("set_A.symmetric_difference(set_B): ", set_A.symmetric_difference(set_B))
print("set_B.symmetric_difference(set_A): ", set_B.symmetric_difference(set_A))

print("---\n1 in set_A: ", 1 in set_A)
print("1 not in set_B: ", 1 not in set_B)

for i in set_A:
    print(i)

for letter in set("banana"):
    print(letter)

frozenset_A = frozenset({1, 2, 3})  # {}
frozenset_B = frozenset({2, 4, 5})
print("frozenset_A | frozenset_B: ", frozenset_A | frozenset_B)
print("frozenset_A & frozenset_B: ", frozenset_A & frozenset_B)
frozenset_A = frozenset([1, 2, 3])  # []
frozenset_B = frozenset([2, 4, 5])
print("frozenset_A | frozenset_B: ", frozenset_A | frozenset_B)
print("frozenset_A & frozenset_B: ", frozenset_A & frozenset_B)
