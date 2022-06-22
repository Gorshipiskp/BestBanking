import os
import time
import random


class misc:

    def __init__(self):
        pass

    def get_time_stamp(months: dict, days_of_week: dict) -> str:
        return f"{time.asctime().replace('Mon', days_of_week.get('Monday')).replace('Sun', days_of_week.get('Sunday')).replace('Tue', days_of_week.get('Tuesday')).replace('Wed', days_of_week.get('Wednesday')).replace('Thu', days_of_week.get('Thursday')).replace('Fri', days_of_week.get('Friday')).replace('Jan', months.get('January')).replace('Feb', months.get('February')).replace('Mar', months.get('March')).replace('Apr', months.get('April')).replace('May', months.get('May')).replace('Jun', months.get('June')).replace('Jul', months.get('Jule')).replace('Aug', months.get('August')).replace('Sep', months.get('September')).replace('Oct', months.get('October')).replace('Nov', months.get('November')).replace('Dec', months.get('December'))}"

    def file_exists(file: str):
        try:
            open(file, "r")
        except:
            return False
        else:
            return True

    def listtostr(list: list):
        itog = ""
        for n in list:
            itog += n
        return itog

    def existel(mass, id):
        try:
            a = mass[id]
            return True
        except:
            return False

    def isfloat(number: any):
        try:
            float(number)
        except:
            return False
        else:
            return True

    def strfind(text: str, symb=" ", rangnumtext=1):
        x = 0
        if len(symb) > len(text):
            return False

        masssymb = []
        itog = ""

        for n in range(0, len(text)):
            masssymb.append(text[n])

        for n in range(0, len(masssymb)):
            if masssymb[n] == symb:
                x += 1
                if x == rangnumtext:
                    return itog
                elif x > rangnumtext:
                    return "awddw2"
            itog += masssymb[n]

    def findword(text: str, word, bool, rngword):
        ln = len(word)
        x = 0
        y = 0

        text = list(text)

        for i in range(0, len(text)):
            if text[i - y] == "\n":
                text.pop(i - y)
                y += 1

        def popoa(text: str):
            c = ""
            for b in range(0, ln):
                if a < (len(text) - ln):
                    c += text[a + b]
                if c == word:
                    if bool:
                        return c, (a - 1)
                    else:
                        return c, (a + ln - 1)
                else:
                    for u in range(0, (a + ln - 1)):
                        text.pop(0)
                    print(text)
                    popoa(text)

        for a in range(0, len(text)):
            while x < rngword:
                c, num = popoa(text)
                if c == word:
                    if bool:
                        return a - 1
                    else:
                        return a + ln - 1
                else:
                    popoa(c)
                x += 1

    def findwordall(text: str, word):
        all = 0
        for a in range(0, len(text)):
            ln = len(word)
            c = ""
            for b in range(0, ln):
                if a < (len(text) - ln):
                    c += text[a + b]
            if c == word:
                all += 1
        return all

    def strfindr(text: str, symb=" "):

        if len(symb) > len(text):
            return False

        masssymb = []
        itog = ""

        for n in range(0, len(text)):
            masssymb.append(text[n])

        masssymb = masssymb[::-1]

        for n in range(0, len(masssymb)):
            if masssymb[n] == symb:
                itog = itog[::-1]
                return itog
            itog += masssymb[n]

    def logmes(dir="Logs", file="NOT TIME", fileex="log", *messages):
        stlog = ""
        if not os.path.exists(dir):
            os.mkdir(dir)
        if not os.path.exists(dir + "/" + file + "." + fileex):
            open(dir + "/" + file + "." + fileex, "w+")

        for n in range(0, len(messages)):
            if n == len(messages) - 1:
                stlog += str(messages[n])
            else:
                stlog += str(messages[n]) + " "

        wfilelog = open(dir + "/" + file + "." + fileex, "r")
        lnth = len(wfilelog.readlines())
        wfilelog.close()

        wfilelog = open(dir + "/" + file + "." + fileex, "a")
        if lnth == 0:
            wfilelog.write(stlog)
        else:
            wfilelog.write("\n" + stlog)
        wfilelog.close()

    def rotmass90(mass):
        newmass = []
        lenm = []
        len2 = len(mass)

        for n in range(0, len(mass)):
            lenm.append(len(mass[n]))

        for n in range(0, max(lenm)):
            newmass.append([])

        for n in range(0, len(newmass)):
            if not (misc.existel(mass, n)):
                mass.append([])
            for m in range(0, len(newmass[n])):
                if not (misc.existel(mass[n], m)):
                    mass[n].append([])

        for n in range(0, len(mass)):
            if not (misc.existel(newmass, n)):
                newmass.append([])

        for m in range(0, max(lenm)):
            for n in range(0, len2):
                if misc.existel(mass[n], m):
                    newmass[m].append(mass[n][m])
                else:
                    newmass[m].append("")
            newmass[m] = newmass[m][::-1]

        return newmass

    def fndwordbyletter(maxstr, boolmax, sym, numsym):
        w = open("russian_edited_to_super_master_pizdec_low.txt", "r")
        mass = w.readlines()
        w.close()
        mass2, mass3 = [], []

        if not (len(sym) == len(numsym)):
            return False

        for i in range(0, len(sym)):
            for n in range(0, len(mass)):
                mass[n] = mass[n].replace("\n", "")
                if (len(mass[n]) == maxstr) and boolmax:
                    try:
                        if mass[n][numsym[i] - 1] == sym[i]:
                            mass2.append(mass[n])
                    except:
                        pass

                elif (len(mass[n]) <= maxstr) and not boolmax:
                    try:
                        if mass[n][numsym[i] - 1] == sym[i]:
                            mass2.append(mass[n])
                    except:
                        pass

                for n in range(0, len(mass2)):
                    word = ""
                    for p in range(0, len(mass2[n])):
                        if p == 0:
                            word += mass2[n][p].upper()
                        else:
                            word += mass2[n][p]
                    mass2[n] = word

        def checkword(mass2, sym, symnum, i, n):
            symnum = symnum[n] - 1
            if mass2[i][symnum].lower() == sym[n].lower():
                return True
            else:
                return False

        for i in range(0, len(mass2)):
            bln = True
            for n in range(0, len(sym)):
                if not bln:
                    break
                bln = checkword(mass2, sym, numsym, i, n)
            if bln:
                mass3.append(mass2[i])

        if len(mass3) == 0:
            return False
        return mass3

    def izdesyat(num: int, sts):
        ost, mas = num, []
        while ost > (sts - 1):
            mas.append(ost % sts)
            ost //= sts
        mas.append(ost % sts)
        mas, st = mas[::-1], ""
        for n in range(0, len(mas)):
            st += str(mas[n])
        st = st.replace(".0", "")
        return st

    def izluboy(num, sts, sts2):
        des = float(misc.vdesyat(num, sts))
        ndes = float(misc.izdesyat(des, sts2))
        return ndes

    def vdesyat(num, sts2):
        mas2, itgn = list(str(num)), 0
        if "e" in mas2:
            return num
        for i in range(0, len(mas2)):
            if mas2[i] == ".":
                mas2.pop(i)
                mas2.pop(i)
                break
        for n in range(0, len(mas2)):
            itgn += float(mas2[n]) * ((sts2 ** (len(mas2) - n)) / sts2)
        return itgn

    def cypher(num):
        nw2 = 10 ** 16
        while nw2 > 10 ** 15:
            x = random.randint(2, 9)
            nw2 = misc.izdesyat(num, x)
            y = random.randint(2, 4)
            nw2 = nw2 * y
            u = x
            while u == x:
                u = random.randint(2, 9)
            nw2 = misc.izluboy(nw2, x, u)
            nw2 = misc.vdesyat(nw2, u)
        return nw2

    def dotsnum(num: float or int):
        number = str(num)[::-1]
        result = ''
        for i, num in enumerate(number):
            if i % 3 == 0:
                result += '.'
            result += num
        result = result[::-1][:-1]
        return result
