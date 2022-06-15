try:
    name = 'John'
    year_born = 'ww'
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)