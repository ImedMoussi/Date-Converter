import math


def int_part(num):
    if num < -0.0000001:
        return math.ceil(num - 0.0000001)
    return math.floor(num + 0.0000001)


def geo2hij(yr, mth, dy):
    jd1 = int_part((1461 * (yr + 4800 + int_part((mth - 14) / 12.0))) / 4)
    jd2 = int_part((367 * (mth - 2 - 12 *  (int_part((mth - 14) / 12.0)))) / 12)
    jd3 = int_part((3 * (int_part((yr + 4900 + int_part((mth - 14) / 12.0)) / 100))) / 4)
    jd = jd1 + jd2 - jd3 + dy - 32075
    l = jd - 1948440 + 10632
    n = int_part((l - 1) /10631.0)
    l = l - 10631 * n + 354
    j1 = (int_part((10985 - l) / 5316.0)) * (int_part((50 * l) / 17719.0))
    j2 = (int_part(l / 5670.0)) * (int_part((43 * l) / 15238.0))
    j = j1 + j2
    l1 = (int_part((30 - j) / 15.0)) * (int_part((17719 * j) / 50.0))
    l2 = (int_part(j / 16.0)) * (int_part((15238 * j) / 43.0))
    l = l - l1 - l2 + 29
    m = int_part((24 * l) / 709.0)
    y = 30 * n + j - 30
    d = l - int_part((709 * m) / 24.0)
    return d, m, y


def hij2geo(yr, mth, dy):
    jd1 = int_part((11 * yr + 3) / 30.0)
    jd2 = int_part((mth - 1) / 2.0)
    jd = jd1 + 354 * yr + 30 * mth - jd2 + dy + 1948440 - 385
    l = jd + 68569
    n = int_part((4 * l) / 146097.0)
    l = l - int_part((146097 * n + 3) / 4.0)
    i = int_part((4000 * (l + 1)) / 1461001.0)
    l = l - int_part((1461 * i) / 4.0) + 31
    j = int_part((80 * l) / 2447.0)
    d = l - int_part((2447 * j) / 80.0)
    l = int_part(j / 11.0)
    m = j + 2 - 12 * l
    y = 100 * (n - 49) + i + l
    return d, m, y

if __name__ == '__main__':
    print("1. Convertir une date du calendrier Julien-Grégorien en date du calendrier Hégire Arabe.")
    print("2. Convertir une date du calendrier Hégire Arabe en date du calendrier Julien-Grégorien.")
    while True:
        answer = input("\nRéponse: ")
        if answer == '1':
            year = int(input("-Année: "))
            month= int(input("-Mois: "))
            day = int(input("-Jour: "))
            hijri = geo2hij(year, month, day)
            print(hijri)

        elif answer == '2':
            year = int(input("-Année: "))
            month= int(input("-Mois: "))
            day = int(input("-Jour: "))
            geo = hij2geo(year, month, day)
            print(geo)
