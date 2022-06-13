from copy import copy


dic  = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# accessing items in a dictionary
first = dic['key1']

# adding new values
# dic["key5"]= "value5"

# modifying values
# dic["key1"]=22

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

dic.pop('key1')
dic.popitem()
del dic['key2']
# we can turn a dictionary into a list of tuples
dic_to_tuples = dic.items()

# copy
dic_copy = dic.copy()

print(dic_copy )
