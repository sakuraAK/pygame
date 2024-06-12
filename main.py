import python101.strings as strings
import python101.functions as foos
from python101.classes import Person, SalariedPerson
from python101 import my_avg


if __name__ == "__main__":
    # strings.count_vowels()
    # strings.count_unique_vowels()
    # strings.is_letters_only()
    # count_vowels_1()
    # is_letters_only()
    # to_capital()
    # foos.default_f(100, "Celsius" )
    # print(foos.my_avg(2, 3))
    # print(foos.my_avg(2, 3, 5))
    # print(foos.my_avg(2, 3, 6, 9))
    #
    # foos.my_car_desc(model="WRX", make="Subaru")
    # foos.my_car_desc(model="WRX")
    # foos.my_car_desc(make="Subaru")
    #
    # average, first_line = foos.my_avg(2, 3)
    # print(average)
    # print(first_line)


    # val = foos.iter(10)
    # print(val)
    #
    # for i in val:
    #     print('here')
    #     print(i)

    volunteer = Person()
    full_time_employee = SalariedPerson(10000)

    employees = [volunteer, full_time_employee]

    for e in employees:
        e.get_details()