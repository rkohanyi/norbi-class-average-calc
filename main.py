import sys

OTOS_PERCENT = 81.0
NEGYES_PERCENT = 71.0
HARMAS_PERCENT = 61.0
KETTES_PERCENT = 41.0

GRADE_PERCENTS = {
    '5': [81.0, 100.0],
    '4': [71.0, 81.0],
    '3': [61.0, 71.0],
    '2': [41.0, 61.0],
    '1': [0.0, 41.0],
}

GRADE_LABELS = {
    'five': 'Ötös',
    'four': 'Négyes',
    'three': 'Hármas',
    'two': 'Kettes',
    'one': 'Egyes',
}

def get_class_name():
    return input('Irja be az osztály nevét !\n')

def get_max_point():
    try:
        return int(input('Adja mag a maximálisan elérhető pontszámot!\n'))
    except:
        print('Adjon meg számot!')
        sys.exit(-1)

def get_curr_point():
    return float(input('Adja meg a pontszámot vagy nyomjon entert az eredményhez!\n'))

def readStatsFromFile(class_name):
    mystat = open('{}.txt'.format(class_name))
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
    print("%s %s %s %.2f %s" % ("A", class_name, "osztály jelenlegi átlaga", atlag2, "!"))
    print("%d%s" % (egyesek, "db Egyes született!"))
    print("%d%s" % (kettesek, "db Kettes született!"))
    print("%d%s" % (harmasok, "db Hármas született!"))
    print("%d%s" % (negyesek, "db Négyes született!"))
    print("%d%s" % (otosok, "db Ötös született!"))


def writeStatsToFile(class_name, szazalek):
    statisztika = open('{}.txt'.format(class_name), 'a+')
    statisztika.writelines(jegyek(szazalek))
    statisztika.close()


def jegyek(szazalek):
    for grade, limits in GRADE_PERCENTS.items():
        lower_percent = limits[0]
        upper_percent = limits[1]
        if lower_percent < szazalek and upper_percent <= szazalek:
            return grade
    raise ValueError('Többet írtál be a maximum pontszámnál!')

    if OTOS_PERCENT < szazalek:
        jegy = "5"
        return jegy
    elif szazalek < OTOS_PERCENT and szazalek > NEGYES_PERCENT:
        jegy = "4"
        return jegy
    elif szazalek < NEGYES_PERCENT and szazalek > HARMAS_PERCENT:
        jegy = "3"
        return jegy
    elif szazalek < HARMAS_PERCENT and szazalek > KETTES_PERCENT:
        jegy = "2"
        return jegy
    elif KETTES_PERCENT >= szazalek:
        jegy = "1"
        return jegy


def hanyas(szazalek):
    if OTOS_PERCENT < szazalek:
        print("Ötös")
    elif szazalek < OTOS_PERCENT and szazalek > NEGYES_PERCENT:
        print("Négyes")
    elif szazalek < NEGYES_PERCENT and szazalek > HARMAS_PERCENT:
        print("Hármas")
    elif szazalek < HARMAS_PERCENT and szazalek > KETTES_PERCENT:
        print("Kettes")
    elif KETTES_PERCENT >= szazalek:
        print("Egyes")


def show_grading_scheme(maxPoint):

    print("%.0f%s%.0f%s%s" % (round(maxPoint * OTOS_PERCENT / 100, 10), "Pont- ", round(maxPoint * 1, 10), "Pont =", " Ötös"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * NEGYES_PERCENT / 100, 10), "Pont- ", round(maxPoint * OTOS_PERCENT / 100, 10), "Pont =", " Négyes"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * HARMAS_PERCENT / 100, 10), "Pont- ", round(maxPoint * NEGYES_PERCENT / 100, 10), "Pont =", " Hármas"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * KETTES_PERCENT / 100, 10), "Pont- ", round(maxPoint * HARMAS_PERCENT / 100, 10), "Pont =", " Kettes"))
    print("%.0f%s%.0f%s%s" % (round(maxPoint * 0, 10), "Pont- ", round(maxPoint * KETTES_PERCENT / 100, 10), "Pont =", " Egyes"))

def continuously_get_points():
    while True:
        try:
            curr_point = get_curr_point()
        except:
            break


def continuously_record_student():
    pass

def is_there_another_student():
    return 'y' == input("again? y or n!\n")

def show_results(class_name, szazalek, pontszam, maxPoint):
    szazalek = pontszam / maxPoint * 100
    print("########################################################")
    print(pontszam, end="")
    print("Pont")
    print("%.0f %s" % (round(szazalek), "%"))
    hanyas(szazalek)
    print("########################################################")
    writeStatsToFile(class_name, szazalek)
    readStatsFromFile(class_name)
    print("########################################################")

def main():
    class_name = get_class_name()
    maxPoint = get_max_point()
    show_grading_scheme(maxPoint)
    breaker = True
    while breaker == True:
        # resets the values
        pontszam = 0
        szazalek = 0
        while True:
            try:
                pontszam = get_curr_point()      
            except:
                szazalek = pontszam / maxPoint * 100
                show_results(class_name, szazalek, pontszam, maxPoint)
                if is_there_another_student():
                    break
                else:
                    breaker = False
                    break

main()