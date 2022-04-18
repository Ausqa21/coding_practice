"""
even
odd
no_of_test_cases = 0
test_cases = []
output = {}

for x in range(no_of_test_cases):
    test_cases.append(input())

for y in test_cases:
    even = ""
    odd = ""
    for i in range(len(y)):
        if i % 2 == 0:
            even += y[i]
        else:
            odd += y[i]
    output[even] = odd

print(output)
"""

from typing import Dict, List


def x() -> List[Dict]:
    no_of_test_cases = int(input())
    test_cases = []
    output = []

    for _ in range(no_of_test_cases):
        test_cases.append(input())

    for y in test_cases:
        even = ""
        odd = ""
        for i in range(len(y)):
            if i % 2 == 0:
                even += y[i]
            else:
                odd += y[i]
        pairing = {}
        pairing[even] = odd
        output.append(pairing)

    return output
    


if __name__ == "__main__":
    res = x()
    for item in res:
        print(list(item)[0], item[list(item)[0]])