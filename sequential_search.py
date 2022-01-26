import random

def search(from_number, n):
    found = False
    for i in from_number:
        if i == n:
            found = True
            break
    return found


