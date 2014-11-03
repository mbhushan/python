x = 50

def glob():
    global x
    print "x value: ", x
    x = 5
    print "new x value: ", x

glob()
print "current x value: ", x
