from string import ascii_letters, digits
from random import sample

def get_random_password(k=8) -> str:
    all_ = sample(ascii_letters + digits, k)
    return "".join(all_)

print(get_random_password())
