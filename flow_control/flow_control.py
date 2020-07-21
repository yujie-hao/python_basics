# if statement

num = 10
if num != 9:
    print(num, "is not 9")
print("finished here")

# if...else

num = 1
if num / 2 == 0:
    print(num, " is an even number")
else:
    print(num, " is an odd number")

num = 0
if num > 0:
    print(num, " is a positive number")
elif num < 0:
    print(num, " is a negative number")
else:
    print(num, " is zero")

# ternary operators
a = 3
num = 1 if a / 2 == 0 else 0
print("num is:", num)
