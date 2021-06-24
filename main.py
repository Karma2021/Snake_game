magic_number = 5
guess_limit = 3
guess_count = 0
while guess_count <= guess_limit:
    guess = int(input('Guess the magic number ? '))
    guess_count += 1
    if guess == magic_number:
        print('You won !')
        break
else:
    print('You lose')
