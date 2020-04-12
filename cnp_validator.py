""" CNP validator.
Expects a 13 digit number as user input.
It will return a message that says if the input is valid/invalid."""
from datetime import datetime


def check_date(aa, ll, zz):
    month_no_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if aa % 4 == 0 and (aa % 100 != 0 or aa % 400 == 0):
        month_no_of_days[1] = 29
    return 1 <= ll <= 12 and 1 <= zz <= month_no_of_days[ll - 1]


def birth_year(s, aa):
    if s == 3 or s == 4:
        return 18
    elif s == 5 or s == 6:
        return 20
    else:
        return 19


def check_digit(cnp):
    # (A + B) mod C = (A mod C + B mod C) mod C
    partial_sum = 0
    seed = list(map(int, '279146358279'))
    counter = 0
    for i in cnp:
        partial_sum = partial_sum + ((i * seed[counter]) % 11)
        counter += 1
    return partial_sum % 11 if partial_sum % 11 != 10 else 1


def check_cnp(cnp):
    today = datetime.today().strftime("%d %m %y")
    t_day = int(today[:2])
    t_mon = int(today[3:5])
    t_year = int(today[6:])

    aa = cnp[1] * 10 + cnp[2]
    ll = cnp[3] * 10 + cnp[4]
    zz = cnp[5] * 10 + cnp[6]
    jj = cnp[7] * 10 + cnp[8]

    if len(cnp) != 13:
        return 0
    elif (cnp[0] in [5, 6]) and aa >= t_year and ll >= t_mon and zz > t_day:
        return 0
    elif jj > 52:
        return 0
    else:
        aaaa = birth_year(cnp[0], aa) * 100 + aa
        if check_date(aaaa, ll, zz) == 0:
            return 0
        c = check_digit(cnp[0:12])
        if c != cnp[12]:
            return 0
    return 1


if __name__ == "__main__":
    try:
        cnp = list(map(int, input("CNP:")))
        if check_cnp(cnp) == 0:
            print("Invalid CNP!")
        else:
            print("Valid CNP!")
    except ValueError:
        print("Could not be checked! Only numbers (integers) expected")
