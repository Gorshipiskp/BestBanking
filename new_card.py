import sqlite3
import bank

debug = False

print("")
print("-------------------------------------------------------------------")
print("------------------СОЗДАНИЕ НОВОЙ БАНКОВСКОЙ КАРТЫ------------------")
print("-------------------------------------------------------------------")
print("")

if debug:
    new_card_name = "БестМолодёжная"  # input("Введите название новой карточки: ")
    new_card_desc = "Супер"  # input("Введите описание новой карточки: ")
    new_card_pay = 100000  # input("Введите плату за год новой карточки: ")
    new_card_type = "Дебетовая"  # input("Введите тип новой карточки: ")
    new_card_active = "True"  # input("Введите активность новой карточки: ")
    new_card_limited = "True"  # input("Введите лимитированность новой карточки: ")
else:
    new_card_name = input("Введите название новой карточки: ")
    new_card_desc = input("Введите описание новой карточки: ")
    new_card_pay = input("Введите плату за год новой карточки: ")
    new_card_type = input("Введите тип новой карточки: ")
    new_card_active = input("Введите активность новой карточки: ")
    new_card_limited = input("Введите лимитированность новой карточки: ")

if (new_card_limited == "True") or (new_card_limited == "true") or (new_card_limited == "1") or (new_card_limited == "yes") or (new_card_limited == "Y") or (new_card_limited == "да") or (new_card_limited == "Да"):
    new_card_limited = True
else:
    new_card_limited = False

if (new_card_active == "True") or (new_card_active == "true") or (new_card_active == "1") or (new_card_active == "yes") or (new_card_active == "Y") or (new_card_active == "да") or (new_card_active == "Да"):
    new_card_active = True
else:
    new_card_active = False

db = sqlite3.connect(f"{bank.databasename}.db")
cursor = db.cursor()

for p in cursor.execute(f"SELECT COUNT(*), * FROM {bank.tablecardsname} WHERE id"):
    num_of_cards = p[0]
num_of_cards = num_of_cards or 0
comma = f"INSERT INTO {bank.tablecardsname} VALUES ({'?, '* (bank.number_of_option_cards - 1)} ?);"
cursor.execute(
    comma, (num_of_cards+1, new_card_name, new_card_desc, new_card_pay, new_card_type, new_card_active, new_card_limited))
db.commit()

print("")
print("-------------------------------------------------------------------")
print(f"-----------БАНКОВСКАЯ КАРТА СОЗДАНА ({new_card_name})-----------")
print("-------------------------------------------------------------------")
print("")
