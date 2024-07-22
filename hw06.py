import re
from collections import UserDict
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value:
            raise ValueError("Name is a mandatory field.")


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone(value):
            raise ValueError("Phone number must be 10 digits.")

    @staticmethod
    def validate_phone(phone):
        return re.fullmatch(r'\d{10}', phone) is not None
class Record:
    def __init__(self, name, phones=None):
        self.name = Name(name)
        self.phones = phones if phones else []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones = ", ".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phones}"
class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name.value] = record

    def remove_record(self, name):
        if name in self.records:
            del self.records[name]

    def find_record(self, name):
        return self.records.get(name, None)

    def __str__(self):
        return '\n'.join(str(record) for record in self.records.values())
# Створення нової адресної книги
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)
