fruit = input('type in a fruit please: ')

index = len(fruit)

while index > 0:
    letter = fruit[index-1]
    print(letter)
    index = index - 1
