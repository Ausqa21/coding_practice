"""
constraints
--
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

base case(s)
--

pseudocode
--
calculate x
break string into a list of lists of size x
while true, loop over the list and pick the first, second, third, ... in that order
return final string

012345 67891011
"""

def x(s: str, numRows: int) -> str:
    s_length = len(s)
    sub_s_length = numRows + (numRows - 2)
    d = {}
    
    if numRows == 1:
        return s

    for x in range(s_length):
        mod = x % sub_s_length
        if mod >= numRows:
            if not d.get(str(sub_s_length - mod)):
                d[str(sub_s_length - mod)] = s[x]
            else:
                d[str(sub_s_length - mod)] += s[x]
            continue
        if not d.get(str(mod)):
            d[str(mod)] = s[x]
        else:
            d[str(mod)] += s[x]

    return "".join([str(x) for x in d.values()])

if __name__ == "__main__":
    print(x("PAYPALISHIRING", 4))
    print(x("PAYPALISHIRING", 3))
    print(x("PAYPALISHIRING", 4))