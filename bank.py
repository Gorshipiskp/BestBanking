import time
import sqlite3
import json


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    return f"{year % 100}|{month}"


def get_from_json(filename, ext="json"):
    return json.load(open(f"{filename}.{ext}", "r", encoding="UTF-8"))


def to_latin(text: str):
    for u in range(0, len(list(replaces_tolatin.keys()))):
        text = text.lower().replace(list(replaces_tolatin.values())[u], list(replaces_tolatin.keys())[u])
    return text.title()


def get_cardid_byname(namecard, file="type_cards", ext="json"):
    return list(get_from_json(file, ext).values()).index(namecard) + 1


def get_cardname_byid(idcard, file="type_cards", ext="json"):
    return list(get_from_json(file, ext).values())[idcard - 1]


def zeros_start(*number: int or str) -> str:
    time.sleep(0.1)
    strw = ""
    for i in number[::-1]:
        strw += str(i)
    return f"{'0' * (length_of_id - len(strw))}{strw}"


def get_card(id_card):
    db = sqlite3.connect(f"{databasename}.db")
    cursor = db.cursor()
    a = cursor.execute(f"""SELECT * FROM {tablecardsname} WHERE ID={id_card}""")
    for i in a:
        info_card = i
    info_card = {
        'id': info_card[0],
        'name': info_card[1],
        'decs': info_card[2],
        'pay': info_card[3],
        'type': info_card[4],
        'active': info_card[5],
        "limited": info_card[6],
    }
    return info_card


def get_user(id_card):
    db = sqlite3.connect(f"{databasename}.db")
    cursor = db.cursor()
    a = cursor.execute(f"""SELECT * FROM {tableusersname} WHERE ID={id_card}""")
    for i in a:
        info_user = i
    info_user = {
        'id': info_user[0],
        'login': info_user[1],
        'password': info_user[2],
        'name': info_user[3],
        'city': info_user[4],
        'phone_number': info_user[5],
        "email_address": info_user[6],
        "secret_phrase": info_user[7],
        "blocked": info_user[8],
        "reputation": info_user[9],
    }
    return info_user


databasename = "db_bank"
tablecards_users_name = "cards_users"
tablecardsname = "cards"
tableusersname = "users"

length_of_id = 10
number_of_option_cards = 7
number_of_option_users = 10
number_of_option_users_cards = 11
expiry_months = 40

name_file_regions = "regions"
name_file_to_latin = "latin-russian_dict"

replaces_tolatin = json.load(open(f"{name_file_to_latin}.json", "r"))
regions = json.load(open(f"{name_file_regions}.json", "r"))

try:
    open(f"{databasename}.db", 'r')
except:
    print("База данных отсутствует")
    time.sleep(0.1)
    print("Создание базы данных...")
    open(f"{databasename}.db", 'w+')
    time.sleep(0.5)
    for _ in range(0, 100, 3):
        time.sleep(0.01)
        print(f"{_}%")
    print("База данных создана")

db = sqlite3.connect(f"{databasename}.db")
cursor = db.cursor()
cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablecards_users_name}(
   id INT PRIMARY KEY,
   type INT,
   cardholder TEXT,
   cardholder_name TEXT,
   card_number TEXT,
   blocked BOOL,
   pincode INT,
   account_address TEXT,
   code_phrase TEXT,
   expiredate TEXT,
   CVC INT);
""")

db.commit()

cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tableusersname}(
   id INT PRIMARY KEY,
   login TEXT,
   password TEXT,
   name TEXT,
   city TEXT,
   phone_number TEXT,
   email_address TEXT,
   secret_phrase TEXT,
   blocked BOOL,
   reputation INT);
""")

db.commit()

cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablecardsname}(
   id INT PRIMARY KEY,
   name TEXT,
   description TEXT,
   pay_year INT,
   type TEXT,
   active BOOL,
   limited BOOL);
""")
db.commit()
