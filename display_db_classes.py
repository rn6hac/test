import shelve

from const import SHELVE_NAME

db = shelve.open(SHELVE_NAME)
print(f'{SHELVE_NAME} content')
print('*' * 50)
for key, person in db.items():
    print(f'{key}\n {person}')
print('*' * 50)
