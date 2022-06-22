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

replaces_tolatin = {
    "a": "а",
    "c": "к",
    "d": "д",
    "k": "к",
    "": "ь",
    "": "ъ",
    "e": "е",
    "f": "ф",
    "q": "к",
    "v": "в",
    "w": "в",
    "h": "х",
    "r": "р",
    "t": "т",
    "y": "й",
    "u": "у",
    "i": "и",
    "o": "о",
    "p": "п",
    "j": "джей",
    "l": "л",
    "z": "з",
    "x": "кс",
    "n": "н",
    "c": "ц",
    "g": "г",
    "sh": "ш",
    "sch": "щ",
    "i": "ы",
    "zh": "ж",
    "e": "э",
    "ya": "ы",
    "ch": "ч",
    "s": "с",
    "i": "и",
    "t": "т",
    "b": "б",
    "yu": "ю"
}

regions = {
    "Башкортостан": {'id_city': '81', 'cities': []},
    "Бурятия": {'id_city': '84', 'cities': []},
    "Республика Алтай": {'id_city': '82', 'cities': []},
    "Дагестан": {'id_city': '26', 'cities': []},
    "Ингушетия": {'id_city': '83', 'cities': []},
    "Кабардино-Балкария": {'id_city': '85', 'cities': []},
    "Калмыкия": {'id_city': '91', 'cities': []},
    "Карачаево-Черкесия": {'id_city': '86', 'cities': []},
    "Карелия": {'id_city': '87', 'cities': []},
    "Республика Коми": {'id_city': '88', 'cities': []},
    "Марий Эл": {'id_city': '89', 'cities': []},
    "Мордовия": {'id_city': '98', 'cities': []},
    "Якутия": {'id_city': '90', 'cities': []},
    "Северная Осетия": {'id_city': '92', 'cities': []},
    "Татарстан": {'id_city': '93', 'cities': []},
    "Тыва": {'id_city': '94', 'cities': []},
    "Удмуртия": {'id_city': '95', 'cities': []},
    "Хакасия": {'id_city': '96', 'cities': []},
    "Чечня": {'id_city': '97', 'cities': []},
    "Чувашия": {'id_city': '01', 'cities': []},
    "Алтайский край": {'id_city': '03', 'cities': []},
    "Краснодарский край": {'id_city': '04', 'cities': []},
    "Красноярский край": {'id_city': '05', 'cities': []},
    "Приморский край": {'id_city': '07', 'cities': []},
    "Ставропольский край": {'id_city': '08', 'cities': []},
    "Хабаровский край": {'id_city': '10', 'cities': []},
    "Амурская область": {'id_city': '11', 'cities': []},
    "Архангельская область": {'id_city': '12', 'cities': []},
    "Астраханская область": {'id_city': '14', 'cities': []},
    "Белгородская область": {'id_city': '15', 'cities': []},
    "Брянская область": {'id_city': '17', 'cities': []},
    "Владимирская область": {'id_city': '18', 'cities': []},
    "Волгоградская область": {'id_city': '19', 'cities': []},
    "Вологодская область": {'id_city': '20', 'cities': []},
    "Воронежская область": {'id_city': '24', 'cities': []},
    "Ивановская область": {'id_city': '25', 'cities': []},
    "Иркутская область": {'id_city': '27', 'cities': []},
    "Калининградская область": {'id_city': '29', 'cities': []},
    "Калужская область": {'id_city': '30', 'cities': []},
    "Камчатский край": {'id_city': '32', 'cities': []},
    "Кемеровская область": {'id_city': '33', 'cities': []},
    "Кировская область": {'id_city': '34', 'cities': []},
    "Костромская область": {'id_city': '37', 'cities': []},
    "Курганская область": {'id_city': '38', 'cities': []},
    "Курская область": {'id_city': '41', 'cities': []},
    "Ленинградская область": {'id_city': '42', 'cities': []},
    "Липецкая область": {'id_city': '44', 'cities': []},
    "Магаданская область": {'id_city': '46', 'cities': []},
    "Московская область": {'id_city': '47', 'cities': []},
    "Мурманская область": {'id_city': '22', 'cities': []},
    "Нижегородская область": {'id_city': '49', 'cities': []},
    "Новгородская область": {'id_city': '50', 'cities': []},
    "Новосибирская область": {'id_city': '52', 'cities': []},
    "Омская область": {'id_city': '53', 'cities': []},
    "Оренбургская область": {'id_city': '54', 'cities': []},
    "Орловская область": {'id_city': '56', 'cities': []},
    "Пензенская область": {'id_city': '57', 'cities': []},
    "Пермский край": {'id_city': '58', 'cities': []},
    "Псковская область": {'id_city': '60', 'cities': []},
    "Ростовская область": {'id_city': '61', 'cities': []},
    "Рязанская область": {'id_city': '36', 'cities': []},
    "Самарская область": {'id_city': '63', 'cities': []},
    "Саратовская область": {'id_city': '64', 'cities': []},
    "Сахалинская область": {'id_city': '65', 'cities': []},
    "Свердловская область": {'id_city': '66', 'cities': []},
    "Смоленская область": {'id_city': '68', 'cities': []},
    "Тамбовская область": {'id_city': '28', 'cities': []},
    "Тверская область": {'id_city': '69', 'cities': ["Тверь"]},
    "Томская область": {'id_city': '70', 'cities': []},
    "Тульская область": {'id_city': '71', 'cities': []},
    "Тюменская область": {'id_city': '73', 'cities': []},
    "Ульяновская область": {'id_city': '75', 'cities': []},
    "Челябинская область": {'id_city': '76', 'cities': []},
    "Забайкальский край": {'id_city': '78', 'cities': []},
    "Ярославская область": {'id_city': '45', 'cities': []},
    "Москва": {'id_city': '40', 'cities': []},
    "Санкт-Петербург": {'id_city': '99', 'cities': []},
    "Еврейская автономная область": {'id_city': '35', 'cities': []},
    "Республика Крым": {'id_city': '111', 'cities': []},
    "Ненецкий автономный округ": {'id_city': '71100', 'cities': []},
    "Ханты-Мансийский автономный округ — Югра": {'id_city': '77', 'cities': []},
    "Чукотский автономный округ": {'id_city': '71140', 'cities': []},
    "Ямало-Ненецкий автономный округ": {'id_city': '67', 'cities': []},
    "Севастополь": {'id_city': '55', 'cities': []},
}

try:
    open(f"{databasename}.db", 'r')
except Exception:
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

newname = get_card(2)["name"]
