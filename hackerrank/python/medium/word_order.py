"""
constraints
--
1 <= n <= 10 ** 5
The sum of the lengths of all the words do not exceed 10 ** 6
All the words are composed of lowercase English letters only.

base case(s)
--
if n == 1, print 1 for count, and 1 for value

pseudocode
--
input: []
output = []
temp = []

capture n

if len(n) == 1:
    print(1)
    print(1)
    return

capture all inputs into input

for word in input:
    if word in temp:
        continue
    else:
        word_count = input.count(word)
        output.append(word_count)
        temp.append(word)

print(len(output))
print(" ".join(output))
"""
import time

def x() -> None:
    inputs = []
    temp = []
    output = []

    n = int(input())

    if n == 1:
        print(1)
        print(1)
        return
    
    for _ in range(n):
        inputs.append(input())

    start = time.perf_counter()
    
    for word in inputs:
        if word in temp:
            continue
        else:
            word_count = inputs.count(word)
            output.append(str(word_count))
            temp.append(word)
    
    print(len(output))
    print(" ".join(output))

    end = time.perf_counter()
    print(end - start)


def x_fast() -> None:
    inputs = []
    # temp = []
    # output = []

    n = int(input())

    if n == 1:
        print(1)
        print(1)
        return

    inputs = [input() for _ in range(n)]
    
    # for _ in range(n):
    #     inputs.append(input())
    # start = time.perf_counter()

    map = {}
    
    for word in inputs:
        if word in map:
            map[word] += 1
        else:
            map[word] = 1
    
    print(len(map))
    print(" ".join([str(y) for y in map.values()]))

    # end = time.perf_counter()
    # print(end - start)


if __name__ == "__main__":
    x_fast()
    # x()

    """
    corner cases
    --
    1. same strings
    
    """
    


