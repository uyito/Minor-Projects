import random

guess = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num_guessed = random.choice(guess)
guesses = 0
num_of_guess = 3
# print(num_guessed)
while guesses < num_of_guess:
    picked = int(input("Guess the number: "))

    if picked == num_guessed:
        print('You guessed right')
        break

    else:
        print('You guessed wrong! Try again.')
        print('')

    guesses = guesses + 1

else:
    print('You used your guesses. You didnt guess right')
    print('the right number is ', num_guessed)
