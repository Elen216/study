nums = input("Введіть три числа через кому: ")

a, b, c = map(float, nums.split(","))

average = (a + b + c) / 3

print("Середнє:", average)
