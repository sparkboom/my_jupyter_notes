import random
import string

def random_password(l):
    return ''.join(random.choices(string.ascii_letters, k=l))