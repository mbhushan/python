zoo = ('python', 'elephant', 'penguin')
print 'Number of animals in the zoo is:',len(zoo)

new_zoo = 'monkey','camel',zoo
print 'Number of cages in the new zoo is: ', len(new_zoo)
print 'All animals in new zoo are: ', new_zoo
print 'animals from old zoo are: ', new_zoo[2]
print 'Last animal from old zoo are: ', new_zoo[2][2]
print 'Total animals in new zoo are', \
    len(new_zoo)-1 + len(new_zoo[2])

