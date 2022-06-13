empty_tupe = ()
new_tuple = (1,2,"three",['four'])

tuple_length = len(new_tuple)

# accessing tuple items
# same as lists 😉 but immutable
first = new_tuple[0]

# slicing 
# same as lists 😉 but immutable .... duh
sliced = new_tuple[1:3]

# check items in a tuple
is_in_tuple = 1 in new_tuple

# joining tuples
sec = ('lory',"dan")
joined = new_tuple + sec

# changing tuples to lists
changed = list(new_tuple)

# deleting tuples
# you can only delete/exterminate a tuple...you cant delete an item because tuples are immutable



# --------------------------------
# exercise
tup = (1,2,3,4,5,6,7,8,9,10)
one,two,three,*rest = tup
print(one)



