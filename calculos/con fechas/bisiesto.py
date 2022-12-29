def separate():
    lst = []
    data = input('please type here the number of year that you want know if is leap: ')
    for i in data:
        lst.append(int(i))
    return lst


Data = separate()
print(Data)


def unit(LST):
    l1 = str(LST[2])
    l2 = str(LST[3])
    lf = l1 + l2
    return lf


Year = unit(Data)
print(Year)


def calculating(YEAR):
    digit = int(YEAR)
    if digit % 4 == 0 and digit % 100 != 0 or digit % 400 == 0:
        result = "Is a leap year"
    else:
        result = "Is not a leap year"

    return result


finalR = calculating(Year)
print(finalR)
