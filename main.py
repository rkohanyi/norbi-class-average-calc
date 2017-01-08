# Asks for a max point and makes sure its a number
while True:
    try:
        osztaly = input("Irja be az osztály nevét !        ")
        maxPoint = int(input("Adja mag a maximálisan elérhető pontszámot        "))
        break
    except:
        print("AZ NEM EGY SZÁM !!!!!!!!!")

# The rules of the marks
otos = 81.0
negyes = 71.0
harmas = 61.0
kettes = 41.0

def readStatsFromFile():
    mystat = open(osztaly + ".txt", "r")
    array = (mystat.read())
    mystat.close()
    stat = []
    atlag = 0

    for i in array:
        stat.append(i)
    for i in stat:
        atlag += int(i)

    egyesek = 0
    kettesek = 0
    harmasok = 0
    negyesek = 0
    otosok = 0

    for i in array:
        if i == "1":
            egyesek += 1
        elif i == "2":
            kettesek += 1
        elif i == "3":
            harmasok += 1
        elif i == "4":
            negyesek += 1
        elif i == "5":
            otosok += 1

    atlag2 = atlag / len(stat)
    print("%s %s %s %.2f %s" % ("A", osztaly, "osztály jelenlegi átlaga", atlag2, "!"))
    print("%d%s" % (egyesek, "db Egyes született!"))
    print("%d%s" % (kettesek, "db Kettes született!"))
    print("%d%s" % (harmasok, "db Hármas született!"))
    print("%d%s" % (negyesek, "db Négyes született!"))
    print("%d%s" % (otosok, "db Ötös született!"))

def writeStatsToFile():
    statisztika = open(osztaly + ".txt", "a+")
    statisztika.writelines(jegyek())
    statisztika.close()

# A function that prints out the appropiate mark based on the ruleset
def jegyek():
    if otos < szazalek:
        jegy = "5"
        return jegy
    elif szazalek < otos and szazalek > negyes:
        jegy = "4"
        return jegy
    elif szazalek < negyes and szazalek > harmas:
        jegy = "3"
        return jegy
    elif szazalek < harmas and szazalek > kettes:
        jegy = "2"
        return jegy
    elif kettes >= szazalek:
        jegy = "1"
        return jegy

def hanyas():
    if otos < szazalek:
        print("Ötös")
    elif szazalek < otos and szazalek > negyes:
        print("Négyes")
    elif szazalek < negyes and szazalek > harmas:
        print("Hármas")
    elif szazalek < harmas and szazalek > kettes:
        print("Kettes")
    elif kettes >= szazalek:
        print("Egyes")

def ponthatar():
    print("%.0f%s%.0f%s%s" % (round(maxPoint * otos / 100, 10), "Pont- ", round(maxPoint * 1, 10), "Pont =", " Ötös"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * negyes / 100, 10), "Pont- ", round(maxPoint * otos / 100, 10), "Pont =", " Négyes"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * harmas / 100, 10), "Pont- ", round(maxPoint * negyes / 100, 10), "Pont =", " Hármas"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * kettes / 100, 10), "Pont- ", round(maxPoint * harmas / 100, 10), "Pont =", " Kettes"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * 0, 10), "Pont- ", round(maxPoint * kettes / 100, 10), "Pont =", " Egyes"))
ponthatar()
# if its false the entire app stops
breaker = True
while breaker == True:
    # resets the values
    pontszam = 0
    szazalek = 0
    while True:
        try:
            pontszam += float(input("Adja meg a pontszámot vagy nyomjon entert az eredményhez      "))
        except:
            szazalek = pontszam / maxPoint * 100
            print("########################################################")
            print(pontszam, end="")
            print("Pont")
            print("%.0f %s" % (round(szazalek), "%"))
            hanyas()
            print("########################################################")
            writeStatsToFile()
            readStatsFromFile()
            print("########################################################")

            again = input("again? y or n    ")
            # calculation for the next stupid kid (same max points)

            if again == "y":
                break
            # No more stupid kid closes the program
            else:
                breaker = False
                break
