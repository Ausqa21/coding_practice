"""
arr1 = []
set1 = {}
set2 = {}
happiness = 0

for element in arr1, if element in set1, increment happiness by 1, else if element in set2,
decrement happiness by 1, else do nothing. Return happiness
"""

def x():
    happiness = 0
    error_msg = "Array length does not match provided array"

    n, m = list(map(int, input().split()))

    arr1 = list(map(int, input().split()))
    # print(f"n: {n} and arr1: {arr1}")
    if len(arr1) != n:
        raise RuntimeError(error_msg)

    a = set(map(int, input().split()))
    if len(a) != m:
        raise RuntimeError(error_msg)

    b = set(map(int, input().split()))
    if len(b) != m:
        raise RuntimeError(error_msg)

    for element in arr1:
        if element in a:
            happiness += 1
        elif element in b:
            happiness -= 1

    return happiness

if __name__ == "__main__":
    print(x())