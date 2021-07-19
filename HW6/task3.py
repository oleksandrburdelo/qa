def is_prime(devider):
    a = 2
    while devider % a != 0:
        a += 1
    return devider == a


print(is_prime(9))

# Well not bad but issue with naming still present. What is devider?
# Add docstring and annotations
