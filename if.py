
number = 23

guess = int(raw_input('Enter an integer: '))

if guess == number:
    print 'Congrats you guessed it correctly!'
    print '(but you do not win any prizes)'
elif guess < number:
    print 'Nopes! its a lower than the number'
else:
    print 'Nopes! Its a higher than the number'
print 'Done!'

