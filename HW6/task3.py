def is_prime(devider):
    a = 2
    while devider % a != 0:
        a += 1
    return devider == a