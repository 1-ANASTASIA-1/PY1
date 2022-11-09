import string
import random

def get_random_password(n = 8) -> str: # TODO написать функцию генерации случайных паролей
    rand_dig = random.choices(string.digits, k=n)
    rand_low = random.choices(string.ascii_lowercase, k=n)
    rand_upp = random.choices(string.ascii_uppercase, k=n)
    rand_list = rand_upp + rand_low + rand_dig
    return "".join(random.sample(rand_list, n))

print(get_random_password())

