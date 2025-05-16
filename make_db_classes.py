import shelve

import const

db = None
try:
    db = shelve.open(const.SHELVE_NAME)
    print('DB OPENED')
    db.clear()  # чистим базу

    db[const.BOB.name] = const.BOB
    db[const.SUE.name] = const.SUE
    db[const.TOM.name] = const.TOM

finally:
    if db:
        db.close()
        print('DB CLOSED')
