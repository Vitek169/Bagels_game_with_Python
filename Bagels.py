"""Бэйглз, (с) Эл Свэйгарт al@inventwithpyton.com
Дедуктивная логическая игра на угадывание числа по подсказкам.
Код размещен https://nostarch.com/big-book-small-python-projects
Один из вариантов этой игры приведен в книге Invent Your Own
Computer Games with Python на https://nostarch.com/inventwithpython
Теги: короткая, игра, головоломка"""

import random

NUM_DIGITS = 3 
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpyton.com

I am thinking if a {} - digit number with no reperated digits.
Try to guess what it is. Ytrt aue some clues:')
When I say:     Thet means:')
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.

For example, if the secret number was 248 and your guess was 843, the cloues would be Fermi Pico.'''.format(NUM_DIGITS))


    while True: #Основной цикл игры
        #Переменная в которой хрянится секретное число, которое
        secretNum = getSecretNum() #Должен угадать игрок
        print('I have thought up a namber.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Продолжаем итерации до получения правильной догадки:
            while len(guess) != NUM_DIGITS or  not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #Правильно, выходим из цикла.
            if numGuesses > MAX_GUESSES:
                print('You run out of guesses.')
                print('The answer was {}.'.format(secretNum))

            #Спрашиваем у игрока, хочет ли он сыграть еще раз.
            print('Do you want to play again?(Yes or NO)')
            if not input('>').lower.startswith('y'):
                break
    print('Thanks for playing!')


def getSecretNum():
    '''Возвращвет строку из NUM_DIGITS уникальных цифр.'''
    numbers = list('0123456789') #Создает список цифр от 0 до 9.
    random.shuffle(numbers) #Перетасовываем их случайным образом.

    #Берем первый NUM_DIGITS цифр списка для нашего секретного числа:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(nubers[i])
        return secretNum


def getClues(guess, secretNum):
    '''Возвращает строку с подсказками pico, fermi и bagels 
    для полученной на входе пары из догадки и секретного числа'''
    if guess == secretNum:
        return 'You got it'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #Правильная цифра на правильном месте.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #Правильная цифрв не на правильном месте.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' #Правильных цифр нет вообще.
    else:
        #Сортируем подсказки в алфовитном порядке,
        # чтоб их исходный порядок ничего не выдавал.
        clues.sort()
        #Склеиваем список подсказок в одно строковое значение.
        return ' '.join(clues)


