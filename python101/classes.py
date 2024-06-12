class Person:
    def __init__(self):
        self._name = "Andrey"
        self._title = "Instructor"
        self._address = "Montreal"

    def get_details(self):
        print(f"name: {self._name}, tile: {self._title}, address: {self._address}")


class SalariedPerson(Person):

    def __init__(self, salary):
        super().__init__()
        self._salary = salary

    def get_details(self):
        print(f"name: {self._name}, tile: {self._title}, address: {self._address}, salary: {self._salary}")