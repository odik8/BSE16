#!/usr/bin/env python
from modules_package import person_operations


def main():
    list_of_people = []

    while True:
        print("1. Добавить человека")
        print("2. Найти человека по номеру телефона")
        print("3. Вывести список людей")
        print("4. Выйти")
        choice = input("Выберите действие (1/2/3/4): ")

        match choice:
            case '1':
                person_operations.add_person(list_of_people)
            case '2':
                phone_to_find = input("Введите номер телефона для поиска: ")
                found_person = person_operations.find_person_by_phone(list_of_people, phone_to_find)
                person_operations.print_person_info(found_person)
            case '3':
                for _ in list_of_people: person_operations.print_person_info(_)
            case '4':
                print("Программа завершена.")
                break
            case _:
                print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
