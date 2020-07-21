# for loop
nums = [1, 2, 3, 4]
for num in nums:
    print("num: ", num)

# range
print("range(10): ", range(10))
print("range(0, 10): ", range(0, 10))

print("list(range(1, 2)): ", list(range(1, 2)))

for i in range(len(nums) - 1):
    print("num[", i, "]: ", nums[i])

for (i, v) in enumerate(nums):
    print("i: ", i, ", v: ", v)


