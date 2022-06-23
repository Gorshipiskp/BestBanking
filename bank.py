import time
import sqlite3
import json

databasename = "db_bank"
tablecards_users_name = "cards_users"
tablecardsname = "cards"
tableusersname = "users"

length_of_id = 10
number_of_option_cards = 7
number_of_option_users = 11
number_of_option_users_cards = 9
expiry_months = 40
cvc_length = 3

name_file_regions = "regions"
name_file_to_latin = "latin-russian_dict"


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    return f"{year % 100}|{month}"


def get_from_json(filename, ext="json", enc="UTF-8"):
    return json.load(open(f"{filename}.{ext}", "r", encoding=enc))


def to_latin(text: str):
    for u in range(0, len(list(replaces_tolatin.keys()))):
        text = text.lower().replace(list(replaces_tolatin.values())[u], list(replaces_tolatin.keys())[u])
    return text.title()


def get_cardid_byname(namecard, file="type_cards", ext="json"):
    return list(get_from_json(file, ext).values()).index(namecard) + 1


def get_cardname_byid(idcard, file="type_cards", ext="json"):
    return list(get_from_json(file, ext).values())[idcard - 1]


def zeros_start(*number: int or str, numnum=length_of_id) -> str:
    time.sleep(0.1)
    strw = ""
    for i in number[::-1]:
        strw += str(i)
    return f"{'0' * (numnum - len(strw))}{strw}"


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


def get_user_card(cardholder_name: str) -> list:
    db_card = sqlite3.connect(f"{databasename}.db")
    cursor_card = db_card.cursor()
    return list(cursor_card.execute(f"""SELECT * FROM {tablecards_users_name} WHERE cardholder_name='{cardholder_name}'"""))


def get_user(id_card: int) -> dict:
    db_user = sqlite3.connect(f"{databasename}.db")
    cursor_user = db_user.cursor()
    a = cursor_user.execute(f"""SELECT * FROM {tableusersname} WHERE ID={id_card}""")
    info_user = {}
    for i in a:
        info_user = i
    try:
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
            "account_id": info_user[10],
        }
        return info_user
    except KeyError:
        return {}


replaces_tolatin = get_from_json(name_file_to_latin, ext="json", enc="Windows-1251")
regions = get_from_json(name_file_regions, ext="json", enc="Windows-1251")

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
   reputation INT,
   account_address TEXT);
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
