"""
first_name
last_name
full_name
output

given $full_name, split it into a list $names. for name in $names, capitalize the name and append
to output, prepended with a space
"""

import random
import string


def solve(s: str) -> str:
    if len(s) <= 0 or len(s) >= 1000:
        raise RuntimeError("String length above limits")

    output = ""
    names = s.split(" ")

    for name in names:
        output += name.capitalize() + " "

    return output.strip()

# CORRECT SOLUTION
def solve_alt(s: str) -> str:
    if len(s) <= 0 or len(s) >= 1000:
        raise RuntimeError("String length above limits")

    output = []
    names = s.split(" ")

    for name in names:
        output.append(name.capitalize())

    return " ".join(output)


if __name__ == "__main__":
    random_string = [''.join(random.choice(string.ascii_lowercase) for _ in range(5)) for _ in range(5)]
    random_string = " ".join(random_string)
    print(solve(random_string))
    print(solve("12abc"))
    print(solve("Abc"))
    print(solve_alt("1 2 2 3 4 5 6 7 8  9"))
    print(solve("1 2 2 3 4 5 6 7 8  9"))
    print(solve_alt("1 2 2 3 4 5 6 7 8  9 ") == solve("1 2 2 3 4 5 6 7 8  9 "))
    while False:
        random_string = [''.join(random.choice(string.ascii_lowercase) for _ in range(5)) for _ in range(5)]
        random_string = " ".join(random_string)
        s = solve(random_string)
        s_alt = solve_alt(random_string)
        print(s, s_alt)

        if s != s_alt:
            print("Mismatch")
            print(s, s_alt)
            break