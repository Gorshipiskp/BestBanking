import sqlite3
import bank

debug = False

print("")
print("-------------------------------------------------------------------")
print("--------------------СОЗДАНИЕ НОВОГО ПОЛЬЗОВАТЕЛЯ-------------------")
print("-------------------------------------------------------------------")
print("")

if debug:
    new_user_login = "Vasiliy Pupkin"
    new_user_password = "opinmnn2223"
    new_user_name = "Пупкин Василий Иванович"
    new_user_city = "Тверь"
    new_user_phone_number = "79520892728"
    new_user_email = "demidovnik2007@gmail.com"
    new_user_secret_phrase = "бестрп"
    new_user_blocked = False
    new_user_reputation = 100
else:
    new_user_login = input("Введите логин нового пользователя: ")
    new_user_password = input("Введите пароль нового пользователя: ")
    new_user_name = input("Введите ФИО нового пользователя: ")
    new_user_city = input("Введите город регистрации нового пользователя: ")
    new_user_phone_number = input("Введите номер телефона нового пользователя: ")
    new_user_email = input("Введите адрес электронной почты нового пользователя: ")
    new_user_secret_phrase = input("Введите секретную фразу нового пользователя: ")
    new_user_blocked = input("Введите статус блокировки нового пользователя: ")
    new_user_reputation = input("Введите репутацию нового пользователя (100 - стандарт): ")

if (new_user_blocked == "True") or (new_user_blocked == "true") or (new_user_blocked == "1") or (new_user_blocked == "yes") or (new_user_blocked == "Y") or (new_user_blocked == "да") or (new_user_blocked == "Да"):
    new_user_blocked = True
else:
    new_user_limited = False

db = sqlite3.connect(f"{bank.databasename}.db")
cursor = db.cursor()

for p in cursor.execute(f"SELECT COUNT(*), * FROM {bank.tableusersname} WHERE id"):
    num_of_users = p[0]
num_of_users = num_of_users or 0
comma = f"INSERT INTO {bank.tableusersname} VALUES ({'?, '* (bank.number_of_option_users - 1)} ?);"
cursor.execute(
    comma, (num_of_users + 1, new_user_login, new_user_password, new_user_name, new_user_city, new_user_phone_number, new_user_email, new_user_secret_phrase, new_user_blocked, new_user_reputation))
db.commit()

print("")
print("-------------------------------------------------------------------")
print(f"-------АККАУНТ ПОЛЬЗОВАТЕЛЯ СОЗДАН ({new_user_name})-------")
print("-------------------------------------------------------------------")
print("")
