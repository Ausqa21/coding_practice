"""
if dict contains name, get marks of name into a variable
find mean of list
print out to 2 decimal places
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name not in student_marks:
        print("Name not in list")
    else:
        marks = student_marks[query_name]
        avg = sum(marks) / len(marks)
        print(format(avg, ".2f"))
