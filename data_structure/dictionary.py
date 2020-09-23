# empty dictionary
my_dict = {}

my_dict = {1: 'apple', 2: 'ball'}

# mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = dict({1: 'apple', 2: 'ball'})  # same as above

my_dict = dict([(1, 'apple'), ('2', 'ball')])  # same as above

print(my_dict[1])
print(my_dict['2'])
print(my_dict.get('2'))
# print(my_dict[3])  # key error: not exist

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)

print(squares.popitem())  # LIFO
print(squares)

print(squares.popitem())
print(squares)

squares.clear()
print(squares)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
del squares
# print(squares) # throws error, reference after del

marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)

for item in marks.items():
    print(item)

print(list(sorted(marks.keys())))

squares = {x: x * x for x in range(10)}
print(squares)

squares = {}
for x in range(6):
    squares[x] = x * x
print(squares)

odd_squres = {x: x * x for x in range(11) if x % 2 == 1}
print(odd_squres)
print(1 in squares)
print(2 not in squares)
print(81 in squares)  # test key only, not for value

#  iterate through
for i in squares:
    print(squares[i])

print(all(squares))
print(all(odd_squres))
print(any(squares))
print(len(squares))
print(sorted(squares))
