friends = ["John", "Marta", "James", "Amanda", "Marianna"]

print('NAME'.center(50, '*'))

for friend in friends:
    print(f'{friend:>20}')

# Good. But done only with f string formatting.
# You should implement with string method too.
# -2 points
