from models import contacts, add_data_to_contacts, find_contact, edit_contact
from collections.abc import Iterator


def start_point() -> None:
    """
    Функция start_point - стартовая точка программы, срабатывает при запуске скрипта и обрабатывает дальнейшие
    действие пользователя :return: None
    """
    first_operation = int(input(
        "Доступные действия с телефонной книгой:"
        "\n1. Вывести контакты телефонной книги"
        "\n2. Добавить новый контакт"
        "\n3. Редактирование контакта"
        "\n4. Поиск записей по заданным характеристикам\n"))
    if first_operation == 1:
        _show_all_contacts_operation()
    elif first_operation == 2:
        _add_new_contact_operation()
    elif first_operation == 3:
        _edit_contact_operation()
    elif first_operation == 4:
        contact = _find_contact_by_parameters()

        f_name, l_name, s_name, organ, per_phone, home_phone = (
            contact["data"]["first_name"], contact["data"]["last_name"],
            contact["data"]["surname"], contact["data"]["organization"],
            contact["data"]["personal_phone"],
            contact["data"]["home_phone"])

        print(f"\nИмя контакта: {f_name}\n"
              f"Фамилия: {l_name}\n"
              f"Отчество: {s_name}\n"
              f"Организация: {organ}\n"
              f"Личный номер: {per_phone}\n"
              f"Домашний номер: {home_phone}\n")


def _show_contacts(generator: Iterator) -> None:
    """
    Функция _show_contacts Принимает на вход генератор
    и при вызове выводит в консоль (если не указаны иной stdout) определенное кол-во контактов (Указаны в генераторе)
    :param generator:
    :return: None
    """
    for contact in next(generator):
        print(f"Имя: {contact['data']['first_name']}")
        print(f"Фамилия: {contact['data']['last_name']}")
        print(f"Отчество: {contact['data']['surname']}")
        print(f"Организация: {contact['data']['organization']}")
        print(f"Личный номер: {contact['data']['personal_phone']}")
        print(f"Домашний номер: {contact['data']['home_phone']}\n")


def _show_all_contacts_operation() -> None:
    """
    Функция _show_all_contacts_operation выполняет операцию 1 (Выводит постранично записи из справочника)
    :return: None
    """
    while True:
        try:
            _show_contacts(contacts)
        except StopIteration:
            print("Телефонных номеров больше нет\n")
            break
        client_answer = input(
            "Для того, чтобы вывести следущую страницу нажмите enter, для того чтобы выйти нажмите q\n")
        if client_answer == 'q':
            break


def _add_new_contact_operation() -> None:
    """
    Функция _add_new_contact_operation выполняет операцию 2 (Добавление новой записи в справочник)
    :return: None
    """
    last_name, first_name, surname = input("Введите фамилию имя и отчество нового контакта:").split()
    organization = input("Введите название организации:")
    personal_phone = input("Введите личный номер телефона:")
    home_phone = input("Введите домашний номер телефона:")
    add_data_to_contacts(first_name, last_name, surname, organization, personal_phone, home_phone)


def _edit_contact_operation() -> None:
    """
    Функция _edit_contact_operation выполняет операцию 3 (Возможность редактирования записей в справочнике)
    :return: dict
    """
    contact = _find_contact_by_parameters()
    last_name, first_name, surname = input("Введите новые фамилию имя и отчество изменяемого контакта:").split()
    organization = input("Введите новое название организации:")
    personal_phone = input("Введите новый личный номер телефона:")
    home_phone = input("Введите новый домашний номер телефона:")
    edit_contact(contact, first_name, last_name, surname, organization, personal_phone, home_phone)


def _find_contact_by_parameters() -> dict:
    """
    Функция _find_contact_by_parameters собирает параметры по которым нужно произвести поиск и передает их в функцию поиска,
    возвращает найденный контакт
    :return: dict
    """
    print("Введите характеристики по которым хотите найти контакт в телефонной книге, "
          "если его нет - оставьте поле пустым")

    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    surname = input("Введите отчество: ")
    organization = input("Введите организацию: ")
    personal_phone = input("Введите номер телефона: ")
    home_phone = input("Введите домашний номер: ")

    contact = find_contact(name, last_name, surname, organization, personal_phone, home_phone)

    return contact


start_point()
