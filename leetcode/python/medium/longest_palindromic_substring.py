"""
constraints
--
1 <= s.length <= 1000
s consist of only digits and English letters.

pseudocode
--
input -> s: str

for x in range(len(s)):
    for y in range(1, len(s) + 1):
        valid_range = s[x: -y]


def isPalindrome(s):
    if s[0] != s[-1]:
        return False
    elif len(s) == 1:
        return True
    else:
        return isPalidrome(s[1:-1])


babad
cP -> F
baba
cP -> F
bab
cp -> T
"""

def y(s: str) -> str:
    output = ""

    if len(s) % 2 != 0:
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pal = s[l: r + 1]
                output = pal if len(pal) > len(output) else output
                l -= 1
                r += 1
    else:
        for i in range(len(s)):
            output = s[i] if len(output) < 1 else output
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pal = s[l: r + 1]
                output = pal if len(pal) > len(output) else output
                l -= 1
                r += 1
    
    return output


def z(s: str) -> str:
    output = ""

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            pal = s[l: r + 1]
            output = pal if len(pal) > len(output) else output
            l -= 1
            r += 1
    
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            pal = s[l: r + 1]
            output = pal if len(pal) > len(output) else output
            l -= 1
            r += 1
    
    return output


def x(s: str):
    memo = {}
    p_substring = ""

    for x in range(len(s)):
        for y in range(len(s[x:])):
            if y == 0:
                # print(s[x:])
                sx = s[x:]
                if sx in memo:
                    if memo[sx]:
                        p_substring = sx if len(sx) > len(p_substring) else p_substring
                        break
                else:
                    res = isPalindrome(sx)
                    memo[sx] = res
                    if res:
                        p_substring = sx if len(sx) > len(p_substring) else p_substring
                        break
            else:
                # print(s[x:-y])
                sxy = s[x:-y]
                if sxy in memo:
                    if memo[sxy]:
                        p_substring = sxy if len(sxy) > len(p_substring) else p_substring
                        break
                else:
                    res = isPalindrome(sxy)
                    memo[sxy] = res
                    if res:
                        p_substring = sxy if len(sxy) > len(p_substring) else p_substring
                        break
    
    return p_substring

def isPalindrome1(s: str):
    # print(f"s is {s} with length: {len(s)}")
    if len(s) == 1 or len(s) == 0:
        return True

    if s[0] != s[-1]:
        return False
    else:
        return isPalindrome1(s[1:-1])

def isPalindrome(s: str) -> bool:
    if len(s) == 1 or len(s) == 0:
        return True

    if s[0] != s[-1]:
        return False
    else:
        if len(s) % 2 == 0:
            left = s[0:len(s) // 2]
            right = s[len(s) // 2:]
            if left == right[::-1]:
                return True
        else:
            midpoint = len(s) // 2
            left = s[0:midpoint]
            right = s[midpoint + 1:]
            if left == right[::-1]:
                return True
    return False

    


if __name__ == "__main__":
    # print(isPalindrome("abba"))
    print(y("abba;lksdflm;vfl;afdskffdaaadl'kfkjlflkvfkldfsalkfdas;kldf';fdlm;kfdjopfjrewpojfkldfkjsdflk;gnejd;lsfvnklafdsfjmvgnskdajdfvvvvvv"))
    print(y(""))
    print(y(" "))
    print(y("ac"))
    print(y("acc"))
    print(("=" * 7))
    print(z("abba;lksdflm;vfl;afdskffdaaadl'kfkjlflkvfkldfsalkfdas;kldf';fdlm;kfdjopfjrewpojfkldfkjsdflk;gnejd;lsfvnklafdsfjmvgnskdajdfvvvvvv"))
    print(z(""))
    print(z(" "))
    print(z("ac"))
    print(z("acc"))