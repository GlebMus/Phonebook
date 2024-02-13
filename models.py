import json
from typing import Optional


def create_contacts_generator() -> dict:
    """
    Функция create_contacts_generator вызвращяет генератор для вывода контактов
    :return: dict
    """
    with open("phonebook.json", "r", encoding="utf-8") as data:
        all_data = json.load(data)
        if len(all_data) > 10:
            for i in range(0, len(all_data), 10):
                print(all_data[i:i + 10])
                yield all_data[i:i + 10]
        else:
            yield all_data


contacts = create_contacts_generator()


def add_data_to_contacts(name: str, last_name: str, surname: str, organization: str,
                         personal_phone: str, home_phone: str) -> None:
    """
    Функция add_data_to_contacts добавляет переданные данные в файл с контактами

    :param name: str,
    :param last_name: str,
    :param surname: str,
    :param organization: str,
    :param personal_phone: str,
    :param home_phone: str,
    :return: None
    """
    try:
        with open("phonebook.json", "r+", encoding='utf-8') as data:
            data.seek(0)
            all_data = json.load(data)
            all_ids = [elem["id"] for elem in all_data]
            data_to_append = {
                "id": all_ids[-1] + 1,
                "data": {
                    "first_name": name,
                    "last_name": last_name,
                    "surname": surname,
                    "organization": organization,
                    "personal_phone": personal_phone,
                    "home_phone": home_phone
                }
            }
            all_data.append(data_to_append)
            data.seek(0)
            json.dump(all_data, data, ensure_ascii=False, indent=4)
            data.truncate()
        print("Данные успешно добавлены")
    except Exception as exp:
        print(f"При добавлении данных произошла ошибка! {exp}")


def find_contact(name: str = '', last_name: str = '', surname: str = '', organization: str = '',
                 personal_phone: str = '', home_phone: str = '') -> Optional[dict, None]:
    """
    Функция find_contact ищет контакт в файле по переданным параметрам

    :param name: str,
    :param last_name: str,
    :param surname: str,
    :param organization: str,
    :param personal_phone: str,
    :param home_phone: str,
    :return: dict or None
    """
    try:
        with open("phonebook.json", "r", encoding="utf-8") as data:
            all_data = json.load(data)
            for contact in all_data:
                if (name and name != contact["data"]["first_name"]) or \
                        (last_name and last_name != contact["data"]["last_name"]) or \
                        (surname and surname != contact["data"]["surname"]) or \
                        (organization and organization != contact["data"]["organization"]) or \
                        (personal_phone and personal_phone != contact["data"]["personal_phone"]) or \
                        (home_phone and home_phone != contact["data"]["home_phone"]):
                    continue
                else:
                    return contact
            print("Такой контакт не найден")
    except Exception as exp:
        print(f"При поиске контакта произошла ошибка!{exp}")


def edit_contact(contact_to_edit: dict, name: str, last_name: str, surname: str,
                 organization: str, personal_phone: str, home_phone: str) -> None:
    """
    Функция edit_contact получет н вход контакт, который надо изменить и меняет его параметры

    :param contact_to_edit: dict,
    :param name: str,
    :param last_name: str,
    :param surname: str,
    :param organization: str,
    :param personal_phone: str,
    :param home_phone: str,
    :return: None
    """
    try:
        with open("phonebook.json", "r+", encoding='utf-8') as data:
            data.seek(0)
            all_data = json.load(data)
            contact_id = contact_to_edit["id"]

            for contact in all_data:
                if contact["id"] == contact_id:
                    contact["data"]["first_name"] = name
                    contact["data"]["last_name"] = last_name
                    contact["data"]["surname"] = surname
                    contact["data"]["organization"] = organization
                    contact["data"]["personal_phone"] = personal_phone
                    contact["data"]["home_phone"] = home_phone
            data.seek(0)
            json.dump(all_data, data, ensure_ascii=False, indent=4)
            data.truncate()
        print("Данные успешно обновлены")
    except Exception as exp:
        print(f"При изменении данных произошла ошибка! {exp}")
