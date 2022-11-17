import random
import string


def randomKey(panjang:int) -> str:
    key = ''.join((random.choice(string.ascii_letters)for i in range(panjang)))
    return key