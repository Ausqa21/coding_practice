"""
input = list of strings, >= 1 and <= 200
input[i].length is >= 0 and <= 200
input[i] consists of only lower-case English letters

def x(arr: List[str]) -> str:
    output = ""
    for x in range(len(arr[0])):
        print(x)
"""

from typing import List


def x(arr: List[str]) -> str:
    output = ""
    starts_with = False
    first_str = arr[0]
    # for x in first_str:
    #     for y in arr[1:]:
    #         if y.startswith(x):
    #             starts_with = True
    #             continue
    #         else:
    #             starts_with = False
    #             break
    #     if starts_with:
    #         output += x
    #         continue
    #     else:
    #         return output
        
    for x in range(len(arr[0])):
        prefix_letter = arr[0][x]
        for item in arr:
            try:
                if not item[x] == prefix_letter:
                    starts_with = False
                    break
                else:
                    starts_with = True
                    continue
            except IndexError as ie:
                starts_with = False
                break
        if starts_with:
            output += prefix_letter
            continue
        else:
            return output
    return output


if __name__ == "__main__":
    print(x(["flo", "flower", "flow"]))
    print(x(["flower","flow","flight"]))
    print(x(["dog","racecar","car"]))
    print(x(["dog","dog","dog"]))
    print(x(["","",""]))
    print(x(["dog"]))
    print(x(["flower", "flow", "flo"]))
    
    a = ["fl" * 100  for _ in range(200)]
    b = ["flower"  for _ in range(200)]

    print(x(a))
    print(x(b))