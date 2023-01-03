import random
again = 'y'
while again == 'y' or again == 'Y':
    for numbers in range(5):
        white_numbers = random.randint(1, 70)
        print(f'White numbers: {white_numbers}')
    red_number = random.randint(1, 27)
    print(f'Red number: {red_number}')
    again = input("Generate again?: ")
