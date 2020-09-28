from functools import cmp_to_key

nums = [1, 2, 5, 4, 3]
nums.sort()
print(nums)

nums = [1, 2, 5, 4, 3]
nums_copy = sorted(nums)
print(nums)
print(nums_copy)

# override __cmp__
nums = [(1, 2), (3, 4), (1, 6)]  # tuples
nums.sort()  # sort by 1st element
print(nums)

nums.sort(key=lambda x: x[1])  # sort by 2nd element
print(nums)

nums.sort(key=lambda x: x[1], reverse=True)  # descendant sort
print(nums)


def cmp(a, b):
    return a - b


nums = [1, 2, 5, 3, 4]
nums.sort(key=cmp_to_key(cmp))
print(nums)

