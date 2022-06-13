a_set = set()

fruits = {'banana', 'orange', 'mango', 'lemon'}
# adding and item in a set
fruits.add('avocado')

# add multiple items
fruits.update(['lime',"cocoa"])
# or
fruits.update('lime',"cocoa")

# remove item
fruits.remove('mango')
# pop() removes a random item
random_fruit = fruits.pop()
print(random_fruit)
