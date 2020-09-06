print('''This is a Guessing Game!
Choose numbers from 1 to 15 
You only have 3 chances.''')
secret_number = 9
i = 1
while i <= 3:
    i += 1
    guess = int(input('Guess the number : '))
    if guess == secret_number:
        print('You Won! 9 was the secret number.')
        break
else:
    print('You have lost the game.')

7