number = 23
running = True
guess = int(input('Введите целое число : '))
while running: 
    if guess == number:
        print('Вы угадали')
        print('поздравляю')
    elif guess < number:
        print('меньше')
    else:
        print('больше')
else:
    print('pfdthityj')
print('Завершение')
