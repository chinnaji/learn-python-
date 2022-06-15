# Packing and Unpacking Arguments in Python
# We use two operators:

# * for tuples
# ** for dictionaries

# numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers)) # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers)      # [2, 3, 4, 5,6]


def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))