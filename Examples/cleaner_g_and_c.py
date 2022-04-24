cube = 8

for guess in range(abs(cube + 1)):
    if guess**3 == abs(cube):
        print('Cube root of ', cube, ' is ', guess)
        break
    if guess != cube:
        print('Guess is not a perfect cube')
    else:
        if guess < 0:
            guess = - guess    
        print('Cube root of ', cube, ' is ', guess)    