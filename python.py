secret_number = 143
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input('Guess the number ? : '))
    guess_count += 1
    if guess == secret_number:
        print('You won !')
        break
else:
    print('You lose')