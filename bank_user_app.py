import PySimpleGUI as psg
import bank
import time

psg.theme('DarkRed2')

debug = True


def login():
    layout = [
        [psg.Text("Номер аккаунта:"), psg.InputText(size=10, font="Comfortaa")],
        [psg.Text("Логин:"), psg.InputText(size=10, font="Comfortaa")],
        [psg.Text("Пароль:"), psg.InputText(size=20)],
        [psg.Button('Войти', font="Comfortaa", key="submit"),
         psg.Button('Выйти', font="Comfortaa", key="cancel")],
        [psg.Text('', font="Comfortaa", key="error", text_color="red")],
        [psg.Text('', font="Comfortaa", key="time")]]

    window = psg.Window("Вход в систему", layout, element_justification='c')

    if __name__ == "__main__":
        while True:
            event, values = window.read(timeout=50)
            window["time"].update(f"{time.strftime('%d.%m.%Y г. %H:%M:%S', time.localtime(time.time()))}")
            if event and not event == "__TIMEOUT__":
                window["error"].update("")
            if event in (psg.WIN_CLOSED, "cancel"):
                window.close()
                return ""
            if event == "submit":
                if not values[0] == "" and not values[1] == "" and not values[2] == "":
                    try:
                        int(values[0])
                    except:
                        window["error"].update("Ошибка в вводе данных")
                        continue

                    user = bank.get_user(values[0])

                    if user == {}:
                        window["error"].update("Аккаунт не найден (номер)")
                        continue

                    if values[1] == user["login"] and values[2] == user["password"]:
                        window.close()
                        return user
                    else:
                        window["error"].update("Неверный логин или пароль")


def main_page(us: dict):
    names = ["ID", "Тип карты", "Носитель карты (Латиница)", "Носитель карты", "Номер карты", "", "", "Номер аккаунта", "", "Дата сгорания", "", "CVC"]
    mass = []
    for massid, i in enumerate(bank.get_user_card(us['name'])):
        mass.append([])
        for ids, u in enumerate(i):
            if not names[ids] == "":
                if names[ids] == "Тип карты":
                    mass[massid].append(psg.Text(f"{names[ids]} - {bank.get_cardname_byid(u)}"))
                else:
                    mass[massid].append(psg.Text(f"{names[ids]} - {u}"))

    layout = [
        [psg.Text(f"Номер аккаунта: {us['id']}")],
        [psg.Text(f"Ваше имя: {us['name']}", auto_size_text=True)],
        [psg.Text(f"Ваши карточки:")],
        [mass],
        [psg.Text('', font="Comfortaa", key="error", text_color="red")],
        [psg.Text('', font="Comfortaa", key="time")]]

    window = psg.Window("Главная", layout, element_justification='c')

    if __name__ == "__main__":
        is_exit = ""
        while True:
            event, values = window.read(timeout=50)
            window["time"].update(f"{time.strftime('%d.%m.%Y г. %H:%M:%S', time.localtime(time.time()))}")
            if event and not event == "__TIMEOUT__":
                window["error"].update("")
            if event in (psg.WIN_CLOSED, "cancel") or is_exit == "cancel":
                break

    window.close()


if not debug:
    user = login()
    if not user == "" and not user == {}:
        main_page(user)
elif debug:
    main_page(bank.get_user(1))
else:
    print("What?")
