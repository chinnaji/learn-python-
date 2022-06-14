from countries import countries,countries_data


# count = 0
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1


# count = 0
# while count < 5:
#     count = count + 1
#     if count == 3:
#         continue
#     print(count)


# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, value) # this way we get both keys and values printed out

# count = 0
# while count < 7:
#     count = count + 1
#     print("#" * count)

# sec_count = 0
# while sec_count < 7:
#     sec_count = sec_count + 1
#     print("#" *8)

# for num in range(1,65):
#     print('#',end=" ")
#     if(num % 8 == 0):
#         print('\n')

# for num in range(1,1000000000000000000000000000):
#     if num % 2 == 0:
#         print('#',end=" ")
#     else:
#         print('*',end=" ")
#         break

# sum = 0
# for num in range(1,101):
#     if num % 2 ==0:
#         pass
#     else:
#         sum += num
# print(sum)

# for country in countries():
#     if "land" in country:
#         print(country) 
#     else:
#         pass

# What are the total number of languages in the data
# language_total = []

# for country in countries_data:
#     for lang in country['languages']:
#         language_total.append(lang)
       
        
# most_spoken_languages = []
# Find the ten most spoken languages from the data
# for num in range(10) :
#     most_spoken_language = max(language_total, key= lambda k: language_total.count(k))
#     most_spoken_languages.append(most_spoken_language)
#     for lang in language_total:
#         if lang in most_spoken_languages:
#             # del language_total[language_total.index(lang)]
#             language_total.remove(lang)
       
    
    #Find the 10 most populated countries in the world
tot_Pops = [pop['population'] for pop in countries_data]
pops_sorted = sorted(tot_Pops, reverse=True)
top_ten = pops_sorted[:10]
    


print(top_ten )


# 
# square = {2: 4, -3: 9, -1: 1, -2: 4}
# a = [1,2,3,4,5,6,7,8,9,10,[11,12]]

# # the key whose value is the largest
# key2 = max(square) #this returns the largest key == 2

# # key (optional) - key function where the iterables are passed and comparison is performed based on its return value
# key2 = max(square, key = lambda param: square[param])

# print("The key whose value is the largest:", key2)    # -3
# print(language_total.count)

# for num in range(0,11):
#     expression = str(num) + ' X ' + str(num) + ' = ' + str(num*num)
#     print(expression)
