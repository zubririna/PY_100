list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

first_max = list_numbers [0]
# начальное значение max
for current_num in list_numbers:
    if current_num > first_max:
        first_max = current_num            # поиск максимального значения

pos_max = list_numbers.index(first_max)    # определение позиции первого max

list_numbers [-1], list_numbers [pos_max] = list_numbers [pos_max], list_numbers [-1]

print(list_numbers)
