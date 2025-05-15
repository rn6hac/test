import shelve

from const import SHELVE_NAME
from person import Person, Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = None
try:
    db = shelve.open(SHELVE_NAME)
    print('DB OPENED')
    db.clear()  # чистим базу

    db['Bob Smith'] = bob
    db['Sue Jones'] = sue
    db['Tom Doe'] = tom

finally:
    if db:
        db.close()
        print('DB CLOSED')
