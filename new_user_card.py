import sqlite3
import bank
import datetime
import random
import PySimpleGUI as psg


psg.theme('DarkAmber')

layout = [
    [psg.Text("Введите тип карты:"), psg.Listbox(list(bank.get_from_json("type_cards").values()),
                                                 size=(20, len(bank.get_from_json("type_cards").values())),
                                                 font="Comfortaa")],
    [psg.Text("Введите номер аккаунта пользователя:"), psg.InputText(size=20)],
    [psg.Text("Введите кодовую фразу:"), psg.InputText(size=20)],
    [psg.Text("Введите статус блокировка:"),
     psg.Listbox(["НЕТ - Блокировка отсутствует", "ДА - Блокировка присутствует"], size=(25, 2), font="Comfortaa")],
    [psg.Text("Введите пинкод:"), psg.InputText(size=10)],
    [psg.Button('Принять', font="Comfortaa", key="submit"),
     psg.Button('Выйти', font="Comfortaa", key="cancel")],
    [psg.Text('', font="Comfortaa", key="info")],
    [psg.Text('', font="Comfortaa", key="error", text_color="red")]]

window = psg.Window("Добавление карточки пользователю", layout)

if __name__ == "__main__":
    while True:
        event, values = window.read()
        if event:
            window["error"].update("")
        if event in (psg.WIN_CLOSED, "cancel"):
            break
        if event == "submit":
            try:
                type_card = bank.get_cardid_byname(values[0][0])
                account_number = values[1]
                code_phrase = values[2]
                is_blocked = values[3][0]
                pin_code = values[4]
                CVC = bank.zeros_start(random.randint(10 ** (bank.cvc_length - 1), int("9" * bank.cvc_length)),
                                       numnum=bank.cvc_length)
                new_card_user_expiry_date = bank.add_months(datetime.datetime.now(), bank.expiry_months)
                new_card_user_name = bank.get_user(account_number).get("name")
                new_card_user_city = bank.get_user(account_number).get("city")
                new_card_user_name_latin = bank.to_latin(new_card_user_name)
                new_card_user_city_id = "NULL"
                for u in range(0, len(bank.regions)):
                    if new_card_user_city in list(bank.regions.values())[u]["cities"]:
                        new_card_user_city_id = list(bank.regions.values())[u]["id_city"]

                if new_card_user_city_id == "NULL":
                    window["error"].update("Ошибка, город выдачи не найден")
                    break

                full_id_number = bank.zeros_start(new_card_user_city_id, account_number)
                if is_blocked == "ДА - Блокировка присутствует":
                    is_blocked = True
                else:
                    is_blocked = False
                db = sqlite3.connect(f"{bank.databasename}.db")
                cursor = db.cursor()
                try:
                    for p in cursor.execute(f"SELECT COUNT(*), * FROM {bank.tablecards_users_name} WHERE id"):
                        num_of_cards = p[0]
                    num_of_cards = num_of_cards or 0
                except:
                    num_of_cards = 0
                comma = f"INSERT INTO {bank.tablecards_users_name} VALUES ({'?, ' * (bank.number_of_option_users_cards - 1)} ?);"
                cursor.execute(comma, (
                    num_of_cards + 1, type_card, new_card_user_name_latin, new_card_user_name,
                    bank.zeros_start(num_of_cards + 1),
                    is_blocked, pin_code, full_id_number, code_phrase, new_card_user_expiry_date,
                    CVC))
                db.commit()
                window["info"].update(
                    f"Карта {type_card} успешно оформлена на {new_card_user_name} - Номер карты {full_id_number}")

            except Exception:
                window["error"].update("Ошибка, попробуйте снова")

window.close()
