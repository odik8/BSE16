from datetime import datetime


def get_birthdate():
    while True:
        try:
            date_str = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
            birthdate = datetime.strptime(date_str, "%d.%m.%Y").date()
            return birthdate
        except ValueError:
            print("Ошибка Неправильный формат даты. Попробуйте снова.")


def add_person(list_of_people):
    print("\nДобавление нового человека:")
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    birthdate = get_birthdate()

    person = {
        'фамилия': last_name,
        'имя': first_name,
        'номер телефона': phone_number,
        'дата рождения': birthdate
    }

    list_of_people.append(person)
    list_of_people.sort(key=lambda x: x['дата рождения'])
    print("Человек добавлен\n")


def find_person_by_phone(people, phone):
    for person in people:
        match person['номер телефона']:
            case phone:
                return person
    return None


def print_person_info(list_of_people):
    match list_of_people:
        case []:
            print("Человек не найден.\n")
        case {'фамилия': f, 'имя': i, 'номер телефона': nt, 'дата рождения': dr}:
            print("\nИнформация о человеке:")
            print(f"Фамилия: {f}")
            print(f"Имя: {i}")
            print(f"Номер телефона: {nt}")
            print(f"Дата рождения: {dr.strftime('%d.%m.%Y')}\n")