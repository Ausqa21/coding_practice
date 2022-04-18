class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

final_output = []
temp_query_count = {"i": 0}

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
        
    temp_query_count["i"] = temp_query_count["i"] + 1
    for _ in range(n):
        x = stream.get_next()
        final_output.append(x)

        local_q = queries
    if temp_query_count["i"] >= local_q:
        print(len(final_output))
        with open("hackerrank/medium/output.txt", "w") as g:
            for y in final_output:
                print(y)
                g.write(str(y) + "\n")

with open('hackerrank/medium/rxt.txt', 'r') as f:
    queries = int(f.readline())
    for _ in range(queries):
        stream_name, n = str(f.readline()).removesuffix("\n").split()
        n = int(n)
        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())

# queries = 2

# queries = int(input())
# for _ in range(queries):
#     stream_name, n = input().split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)
#     else:
#         print_from_stream(n, OddStream())