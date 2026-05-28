def find_unique_value(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num

print(find_unique_value([1,2,1,1]))
