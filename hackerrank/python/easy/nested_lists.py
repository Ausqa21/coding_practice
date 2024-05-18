"""
create nested list
extract scores, remove duplicates and order in ascending order
pick second score
loop and get corresponding names, sort, and print
"""

scores: list = []


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

        scores.append([name, score])

    raw_scores: set = sorted(set([y for [_, y] in scores]))

    second_lowest: float = raw_scores[1]

    names: list[str] = sorted([x for [x, y] in scores if y == second_lowest])

    for i in names:
        print(i)
