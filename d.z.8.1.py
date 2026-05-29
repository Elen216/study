def add_one(digits):
    number_as_string = ""
    for digit in digits:
        number_as_string = number_as_string + str(digit)
    total_sum = int(number_as_string) + 1
    result_as_string = str(total_sum)
    final_list = []
    for character in result_as_string:
        final_list.append(int(character))

    return final_list

# --- Перевірка ---
print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))
