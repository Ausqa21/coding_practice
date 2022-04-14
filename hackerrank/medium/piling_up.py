"""
constaints
--

base cases
--
n == 1, Yes

pseudocode
--
def x(l: List[str], n: int) -> bool:
    output = False
    level = 2 ** 31
    rm_index = 0
    lm_index = -1
    
    for _ in range(n):
        rm = l[rm_index]
        lm = l[lm_index]

        if level is None:
            if rm >= lm:
                level = rm
                rm_index += 1
                output = True
                continue
            else:
                level = lm
                lm_index -= 1
                output = True
                continue
        else:
            if rm > level and lm > level:
                return False

            if rm <= level:
                level = rm
                rm_index += 1
                output = True
                continue

            if lm <= level:
                level = lm
                lm_index -= 1
                output = True
                continue

    return output

if both > level, False
if both < level:
    find greatest, True

"""

from typing import List


def x(l: List[int], n: int) -> str:
    output = "No"
    level = None
    rm_index = 0
    lm_index = -1
    
    for _ in range(n):
        rm = l[rm_index]
        lm = l[lm_index]

        if level is None:
            if rm >= lm:
                level = rm
                rm_index += 1
                output = "Yes"
                continue
            else:
                level = lm
                lm_index -= 1
                output = "Yes"
                continue
        else:
            if rm > level and lm > level:
                # print(level)
                # print(rm, rm_index)
                # print(lm, lm_index)
                # print("here")
                return "No"
            
            if rm <= level and lm <= level:
                value = rm if rm >= lm else lm

                if rm == value:
                    level = rm
                    rm_index += 1
                    output = "Yes"
                    continue
                else:
                    level = lm
                    lm_index -= 1
                    output = "Yes"
                    continue

            if rm <= level:
                level = rm
                rm_index += 1
                output = "Yes"
                continue

            if lm <= level:
                level = lm
                lm_index -= 1
                output = "Yes"
                continue

    return output


if __name__ == "__main__":
    # print(x([4, 3, 2, 1, 3, 4], 6))
    # print(x([1, 3, 2], 3))
    # print(x([1, 2, 3, 8, 7], 5))
    print(x([488028917, 637472922, 617949858], 3))
    # T = int(input())
    # for _ in range(T):
    #     l = []
    #     n = int(input())
    #     l = [int(x) for x in input().split()]
    #     # for _ in range(n):
    #     #     l.append(int(input()))
    #     print(x(l, n))
