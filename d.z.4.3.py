import random

length = random.randint(3, 10)

random_list = [random.randint(1, 100) for _ in range(length)]
new_list = [random_list[0], random_list[2], random_list[-2]]

print(f"Початковий список: {random_list}")
print(f"Новий список: {new_list}")
