#!/bin/python3

# import os

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    # Write your code here
    unique_rank = sorted(list(set(ranked)), reverse=True)

    rank_result = []
    for score in player:
        while len(unique_rank) > 0 and score >= unique_rank[-1]:
            unique_rank.pop()

        rank_result.append(len(unique_rank) + 1)
    return rank_result

    # ranked = list(dict.fromkeys(ranked))
    # # output: list[int] = [0 for _ in range(len(player))]
    # output = []
    # # for i, p in enumerate(player):
    # for p in player:
    #     ranked_new = ranked + [p]
    #     ranked_new.sort(reverse=True)
    #     # print(p, ranked_new)
    #     # print(p, ranked_new_nd)
    #     idx = ranked_new.index(p)
    #     # output[i] = idx + 1
    #     output.append(idx + 1)

    # print(output)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)

    # fptr.write("\n".join(map(str, result)))
    # fptr.write("\n")

    # fptr.close()
