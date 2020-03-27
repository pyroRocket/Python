import string
import random


def generatePassword(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


print(generatePassword(10))
