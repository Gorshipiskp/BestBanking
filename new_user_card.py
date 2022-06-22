import sqlite3
import sys
import bank
import random
import time
import datetime
import calendar


debug = False

db = sqlite3.connect(f"{bank.databasename}.db")
cursor = db.cursor()

for p in cursor.execute(f"SELECT COUNT(*), * FROM {bank.tablecards_users_name} WHERE id"):
    num_of_cards = p[0]
num_of_cards = num_of_cards or 0

print("")
print("-------------------------------------------------------------------")
print("-----------СОЗДАНИЕ НОВОЙ БАНКОВСКОЙ КАРТЫ ПОЛЬЗОВАТЕЛЯ------------")
print("-------------------------------------------------------------------")
print("")

if debug:
    new_card_type = bank.get_cardid_byname("Виртуальная")
    new_card_user_id = 4
    new_card_user_name = bank.get_user(new_card_user_id).get("name")
    new_card_user_city = bank.get_user(new_card_user_id).get("city")
    new_card_user_name_latin = bank.to_latin(new_card_user_name)
    new_card_user_city_id = "NULL"

    for u in range(0, len(bank.regions)):
        if new_card_user_city in list(bank.regions.values())[u]["cities"]:
            new_card_user_city_id = list(bank.regions.values())[u]["id_city"]

    if new_card_user_city_id == "NULL":
        print(f"Ошибка! Код города регистрации не найден ({new_card_user_city})")
        sys.exit()

    full_id_number = bank.zeros_start(new_card_user_city_id, new_card_user_id)
    code_phrase = "secret"
    new_card_user_expiry_date = bank.add_months(datetime.datetime.now(), bank.expiry_months)
    blocked = False
    pincode = 1357
    CVC = 733

else:
    new_card_type = bank.get_cardid_byname(input("Введите тип карты: "))
    new_card_user_id = int(input("Введите номер пользователя: "))
    new_card_user_name = bank.get_user(new_card_user_id).get("name")
    new_card_user_city = bank.get_user(new_card_user_id).get("city")
    new_card_user_name_latin = bank.to_latin(new_card_user_name)
    new_card_user_city_id = "NULL"

    for u in range(0, len(bank.regions)):
        if new_card_user_city in list(bank.regions.values())[u]["cities"]:
            new_card_user_city_id = list(bank.regions.values())[u]["id_city"]

    if new_card_user_city_id == "NULL":
        print(f"Ошибка! Код города регистрации не найден ({new_card_user_city})")
        sys.exit()

    full_id_number = bank.zeros_start(new_card_user_city_id, new_card_user_id)
    code_phrase = input("Введите кодовую фразу: ")
    new_card_user_expiry_date = bank.add_months(datetime.datetime.now(), bank.expiry_months)
    blocked = input("Введите статус блокировки: ")
    pincode = int(input("Введите пинкод: "))
    CVC = int(input("Введите CVC-код: "))

if (blocked == "True") or (blocked == "true") or (blocked == "1") or (
        blocked == "yes") or (blocked == "Y") or (blocked == "да") or (
        blocked == "Да"):
    blocked = True
else:
    blocked = False

comma = f"INSERT INTO {bank.tablecards_users_name} VALUES ({'?, ' * (bank.number_of_option_users_cards - 1)} ?);"

cursor.execute(comma, (num_of_cards+1, new_card_type, new_card_user_name_latin, new_card_user_name, bank.zeros_start(num_of_cards + 1), blocked, pincode, full_id_number, code_phrase, new_card_user_expiry_date,
                       CVC))
db.commit()

print("")
print("------------------------------------------------------------------")
print(f"-----------БАНКОВСКАЯ КАРТА СОЗДАНА ({full_id_number})-----------")
print(f"--------КАРТХОЛДЕР ОБНОВЛЁН ({new_card_user_name_latin})---------")
print("------------------------------------------------------------------")
print("")
