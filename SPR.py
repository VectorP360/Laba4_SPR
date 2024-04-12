from enum import Enum
from abc import abstractmethod

class TelephoneDictionary():
    def __init__(self):
        self.dictionary = {}

    def Add_abonent(self, name: str, telephone: str):
        self.dictionary[name] = telephone
        print (f'Абонент {name} успешно добавлен')

    def Edit_abonent(self, name: str, telephone: str):
        if telephone:
            self.dictionary[name] = telephone
            print(f'Номер телефона абонента {name} успешно изменён')
        else:
            print(f"Абонента {name} не существует")

    def lookup_abonent(self, name: str):
        telephone = self.dictionary.get(name, None)
        if telephone:
            print(f"У абонента {name} номер телефона {telephone}")
        else:
            print(f"Абонента {name} не существует")

    def delete_abonent(self, name: str):
        self.dictionary.pop(name)
        print(f'Абонент {name} успешно удалён')

    def __str__(self):
        ret_dict = ""
        for key, value in self.dictionary.items():
            ret_dict += f'{key}: {value}\n'
        return ret_dict
    
abonents = TelephoneDictionary()
abonents.Add_abonent("Михаил", "+7-900-180-45-54")
abonents.Add_abonent("Влад", "+7-902-440-50-80")
abonents.Add_abonent("Полина", "+7-904-755-89-70")

print(abonents)

abonents.delete_abonent("Михаил")
abonents.Edit_abonent("Влад", "+7-902-452-73-53")
abonents.lookup_abonent("Полина")

print(abonents)