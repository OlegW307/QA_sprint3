import secrets
import string
import random


def gen_pass(number):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(number))
    return password


def gen_login():
    info_list = random.sample(range(3, 30), 2)
    info_list.append(random.randint(2, 6))
    data_list = []
    for i in info_list:
        data_list.append(''.join(random.choice(string.ascii_lowercase) for _ in range(i)))
    return data_list[0] + "@" + data_list[1] + "." + data_list[2]
