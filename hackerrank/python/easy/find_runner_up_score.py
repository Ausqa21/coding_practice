"""
sort list in descending order
create a variable called 'highest' and assign the first element to it
loop from the second element, if it's equal, continue, if it's less,
return that value
"""


def x(a: list) -> int:
    b: list = sorted(a, reverse=True)
    print(b)

    highest: int = b[0]

    for c in range(1, len(b)):
        if b[c] < highest:
            return b[c]
        else:
            continue


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(x(arr))
