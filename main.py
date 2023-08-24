import random


def computer_guess(x):
    global guess
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            low = guess - 1
        elif feedback == 'l':
            high = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly')


computer_guess(100)
