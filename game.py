import random

num = random.randint(0, 100)
guesses = 0
# print(num)

guessed = False

while not guessed:
    ans = int(input('Guess a number: '))
    guesses += 1
    print('You have guessed {} times'.format(guesses))

    if ans == num:
        print('You guessed correctly!')
        print('It took {} tries.'.format(guesses))
        guessed = True
    elif ans > num:
        print('Go lower..')
    elif ans < num:
        print('Go higher....')







