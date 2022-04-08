"""
s: str
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

output: int
temp_substring: List[int]

for char in $s, 
    if $char is already in $temp_substring,
        get the length of $temp_substring as $temp_substring_length
        if $temp_substring_length > $output:
            $output = $temp_substring_length
        empty $temp_substring
        append $char to $temp_substring
        $output += 1
    else
        append $char to $temp_substring
        $output += 1

return $temp_substring

"""

import random
import string


def x(s: str) -> int:
    if len(s) < 0 or len(s) > 5 * 10**4:
        raise RuntimeError("String length out of bounds")

    output = 0
    temp_substring = []

    for x in range(len(s)):
        if s[x] in temp_substring:
            temp_substring_length = len(temp_substring)
            if temp_substring_length > output:
                output = temp_substring_length
            first_index = temp_substring.index(s[x])
            temp_substring = temp_substring[first_index + 1:]
            temp_substring.append(s[x])
        else:
            temp_substring.append(s[x])
    
    return len(temp_substring) if len(temp_substring) > output else output


if __name__ == "__main__":
    print(x("abcabcbb"))
    print(x("  "))
    print(x("aaaaaabbbbbcde"))
    print(x("aa@a(aa#bbb)b!bc&de"))   #[b, ), ]
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
    print(a)
    print(x(a))
    