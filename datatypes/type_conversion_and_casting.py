# ==================================================
"""
https://www.programiz.com/python-programming/type-conversion-and-casting

Key Points to Remember
1. Type Conversion is the conversion of object from one data type to another data type.
2. Implicit Type Conversion is automatically performed by the Python interpreter.
3. Python avoids the loss of data in Implicit Type Conversion.
4. Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
5. In Type Casting, loss of data may occur as we enforce the object to a specific data type.
"""

# ==================================================
# implicit Type Conversion: Implicit Type Conversion is automatically performed by the Python interpreter.

# 1. Converting integer to float: implicit conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int: ", type(num_int))
print("datatype of num_flo: ", type(num_flo))

print("datatype of num_new: ", type(num_new))
print("datatype of num_new: ", type(num_new))

# 2. Addition of string data type and integer datatype --> TypeError
num_int = 123
num_str = "456"
# num_new = num_int + num_str  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print("Data type of num_new: ", type(num_new))
# print("num_new = ", num_new)

# ==================================================

#  Explicit type conversion: <type>(), a.k.a: Type Casting
num_int = 123
num_str = "456"

num_str = int(num_str)
print("Data type of num_str after type casting: ", type(num_str))

num_sum = num_int + num_str
print("Data type of num_sum: ", type(num_sum), ", value: ", num_sum)
