"""
check in haystack contains needle
if no, return -1
else, magic
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("leetcode", "leeto"))
