class Person:
    def __init__(self,
                 name: str,
                 age: int,
                 pay: float = 0.0,
                 job: str | None = None
                 ) -> None:
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self) -> str:
        return self.name.split()[-1]

    def give_raise(self, percent: float) -> None:
        self.pay += self.pay * percent

    def __str__(self):
        return (
            f'{self.__class__.__name__} => {self.name}: {self.job}, {self.pay}'
        )

        # ('<%s => %s: %s, %s>' %


class Manager(Person):

    def __init__(self, name: str, age: int, pay: float) -> None:
        super().__init__(name, age, pay, 'manager')

    def give_raise(self, percent: float, bonus: float = 0.1) -> None:
        super().give_raise(percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(sue, sue.pay, sue.last_name())
    for obj in (bob, sue, tom):
        obj.give_raise(0.10)
        print(obj)
