class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print '(Initializing {0})'.format(self.name)
        Robot.population += 1

    def die(self):
        print '{} is being destroyed!!'.format(self.name)
        Robot.population -= 1
        if (Robot.population == 0):
            print '{} was the LAST ONE!'.format(self.name)
        else:
            print '{} robots are remaining!'.format(Robot.population)
    def say_hi(self):
        print 'Greetings, my masters call me {}'.format(self.name)

    @classmethod
    def how_many(cls):
        print 'We have {:d} robots!'.format(cls.population)

r1 = Robot("R2-D2")
r1.say_hi()
Robot.how_many()

r2 = Robot("C3-P0")
r2.say_hi()
Robot.how_many()

print 'Robots can do some work here!!'
print 'Robots have done some work - so lets destroy them :)'
r1.die()
r2.die()

Robot.how_many()
