shoplist = ['apple','mango','carrot','banana']

print 'I have ',len(shoplist), ' items to purchase!'

print 'These items are: '

for item in shoplist:
    print item

print '\nI have rice to buy as well!'
shoplist.append('rice')

print 'My shopping list is now: ', shoplist

print 'I will sort my shopping list:'

shoplist.sort()

print 'Sorted list is now: ', shoplist

print 'Frist item I will buy is: ', shoplist[0]

first = shoplist[0]
del shoplist[0]

print 'I bought: ', first
print 'My shopping list is now: ', shoplist
