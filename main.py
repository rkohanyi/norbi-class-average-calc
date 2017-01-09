import sys

GRADE_PERCENTS = {
    '5': [82.0, 100.0],
    '4': [72.0, 81.0],
    '3': [62.0, 71.0],
    '2': [42.0, 61.0],
    '1': [0.0, 41.0],
}

GRADE_LABELS = {
    '5': 'Ötös',
    '4': 'Négyes',
    '3': 'Hármas',
    '2': 'Kettes',
    '1': 'Egyes',
}

def calc_percent(point, maxPoint):
    return point * maxPoint / 100


def get_class_name():
    return input('Irja be az osztály nevét !\n')


def get_max_point():
    try:
        return int(input('Adja mag a maximálisan elérhető pontszámot!\n'))
    except:
        print('Adjon meg számot!')
        sys.exit(-1)


def get_curr_point():
    user_input = input('Adja meg a pontszámot vagy nyomjon entert az eredményhez!\n')
    if user_input is '':
        return None
    return float(user_input)


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
        if lower_percent <= szazalek and szazalek <= upper_percent:
            return grade
    raise ValueError('Többet írtál be a maximum pontszámnál!')


def show_grading_scheme(maxPoint):
    for grade, limits in GRADE_PERCENTS.items():
        lower = round(maxPoint * limits[0] / 100, 10)
        upper = round(maxPoint * limits[1] / 100, 10)
        label = GRADE_LABELS[grade]
        sep1 = " Pont- "
        sep2 = " Pont = "
        print("%.0f%s%.0f%s%s" % (lower, sep1, upper, sep2, label))


def is_there_another_student():
    return 'y' == input("again? y or n!\n")

def show_results(class_name, pontszam, maxPoint):
    szazalek = calc_percent(pontszam, maxPoint)
    print("########################################################")
    print(pontszam, end="")
    print("Pont")
    print("%.0f %s" % (round(szazalek), "%"))
    grade = jegyek(szazalek)
    print(GRADE_LABELS[grade])
    print("########################################################")
    writeStatsToFile(class_name, szazalek)
    readStatsFromFile(class_name)
    print("########################################################")


def main():
    class_name = get_class_name()
    maxPoint = get_max_point()
    show_grading_scheme(maxPoint)
    sum_of_points = 0
    while True:
        point = get_curr_point()
        if point is None:
            show_results(class_name, sum_of_points, maxPoint)
            if is_there_another_student():
                sum_of_points = 0
            else:
                break
        else:
            sum_of_points += point


main()