"""
if year is not divisible by 4, return False
else if year is divisible by 100, return False
else if year is divisible by 400, return True
"""


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap


print(is_leap(1992))
