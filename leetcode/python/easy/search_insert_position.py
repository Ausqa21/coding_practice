"""
loop through list, if target is equal to current obj, return index
else if it is less than current obj, return that index
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        y = len(nums)
        for x in range(y):
            if nums[x] >= target:
                return x
        return y


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
