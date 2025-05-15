import shelve

from const import SHELVE_NAME

db = None
try:
    db = shelve.open(SHELVE_NAME, flag='c')
    print('DB OPENED')
    print('-' * 30)
    for full_name, person in db.items():
        print(f'Before raise {person}')
        person.give_raise(0.20)
        print(f'After raise {person}')
        db[full_name] = person
        print(f'{full_name} information was updated')
        print('-' * 30)

finally:
    if db:
        db.close()
        print('DB CLOSED')

