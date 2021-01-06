valid_fruits = ['apple', 'orange', 'pineapple', 'watermelon', 'durian']

with open('data.txt', 'w') as fileptr:
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in valid_fruits:
            fileptr.write(fruit + '\n')
        else:
            break
