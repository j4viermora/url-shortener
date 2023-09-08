from random import randint
from base36 import dumps


def generate_short_url():
    string_code = randint(10000000, 99999999)
    number_code = int(string_code)
    return dumps(number_code)

