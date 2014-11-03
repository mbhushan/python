map = {'mani':'mani.bhushan@vizury.com',
       'archana':'archana.singh.cse@gmail.com',
       'shreyansh':'shreyansh@gmail.com',
       'tv':'tvf@gmail.com',
       'spam':'spam@gmail.com'
       }

print 'Mani\'s email address: ',map['mani']
del map['spam']

print '\nThere are {} contacts in the email address book.'.format(len(map))

for name,email in map.items():
    print 'contact {0} at {1}'.format(name, email)

#adding a name, email to the existing list
map['shona'] = 'shona@gmail.com'

if 'shona' in map:
    print '\nshona\'s email address is: ',map['shona']
