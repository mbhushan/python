
number = 23

running = True

while running:
    guess = int(raw_input('Enter an integer: '))
    if guess == number:
        print 'Yes!! you got the number!!'
        running = False
    elif guess < number:
        print 'Guess is less than the number!'
    else:
        print 'Guess is greater than the number!'
else:
    print 'Loop is over!!!'
print 'Done!'
