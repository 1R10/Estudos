my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print(f'Original dictionary: {my_dict}')
del my_dict['profession']
print(f'\nUpdated dictionary after removing "profession": {my_dict}')

for k,v in my_dict.items():
    print(f'{k}: {v}')

if my_dict['age']:
    verif = True
else:
    verif = False
print(f'\n\nDoes age is in dictionary? {verif}')