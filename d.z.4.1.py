def zeros_to_end(nums):
    non_zeros = [n for n in nums if n != 0]
    zero_count = nums.count(0)
    return non_zeros + [0] * zero_count
# Приклад:
my_list = [1,0,6,0,5,11,0,2]
result =zeros_to_end(my_list)
print(result)
