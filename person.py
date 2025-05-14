""""Dima = {'name': 'Dima Katugin', 'Age': '34', 'Pay': '74500', 'Profession': "TP"}
Viola = {'name': 'Violetta Lapteva', 'Age': '30', 'Pay': '60000', 'Profession': 'HR'}
Viko = {'name': 'Victoriya Shatova', 'Age': '32', 'Pay': '65000', 'Profession': 'BUH'}
people = [Dima, Viola, Viko]
for person in people:
       print(person['name'], person['Pay'], sep=' , ')
#for person in people:
# for (name, value) in person:
#    if name == 'name':
  #   print(value)
#def field(record, label):
#    for (fname, fvalue) in record:
#        if fname == label:
#            return fvalue
# for rec in people:
#    print(field(rec, 'name'))
#for person in people:
#    print(person[0].split()[-1])
#    person[2] *= 1.20
#    print(person[2])
#pays = sum(person[2] for person in people)
#print(pays)
#people.append(["Artur Piroshkov", 32, 150000, "Developers"])
#len(people)
#print(people)
#print(bob[0].split()[1])"""
class Person:
       def __init__(self, name, age, pay=0, job=None):
              self.name = name
              self.age = age
              self.pay = pay
              self.job = job
       def lastName(self):
           return self.name.split()[-1]
       def giveRaise(self, percent):
           self.pay *= (1.0 + percent)
       def __str__(self):
           return  (f' {self.__class__.__name__} => {self.name}: {self.job}, {self.pay}>')

                                                             #('<%s => %s: %s, %s>' %
class Manager(Person):

       def __init__(self, name, age, pay):
              Person.__init__(self, name, age, pay, 'manager')
       def giveRaise(self, percent, bonus=0.1):
              Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
if __name__=='__main__':
       bob = Person('Bob Smith', 42, 30000, 'software')
       sue = Person('Sue Jones', 45, 40000, 'hardware')
       tom = Manager(name='Tom Doe', age=50, pay=50000)
       print(sue, sue.pay, sue.lastName())
       for obj in (bob, sue, tom):
              obj.giveRaise(.10)
              print(obj)



