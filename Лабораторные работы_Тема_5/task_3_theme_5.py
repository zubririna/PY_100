import random

def get_unique_list_numbers() -> list[int]:
    list_=set()
    k = 0
    while len(list_) < 15:
        var = random.randint(-10, 10)
        k+=1
        list_.add(var)
    return list(list_)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
