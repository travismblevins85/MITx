# I may need to import something for this file unless its the exact cube root 
# of the number because it runs thousands of loops at increment .0001, which 
# i can increase, but it would be less accurate, check for import later

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += 1
print('num_guesses = ', num_guesses)

if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of ', cube)

else:
    print(guess, ' is close to the cube root of ', cube)    

# Need to find a better way to solve this solution, maybe later in this lecture    