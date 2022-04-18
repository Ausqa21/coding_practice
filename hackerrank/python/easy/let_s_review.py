from typing import List

def x(arr: List):
    arr.reverse()
    return " ".join([str(a) for a in arr])

if __name__ == "__main__":
    print(x([1,2,3,4,5]))