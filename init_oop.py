class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print 'weclome to python, ', self.name

p = Person('mani bhushan')
p.say_hello()
