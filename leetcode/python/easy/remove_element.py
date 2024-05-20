"""

"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        for _ in range(count):
            nums.remove(val)
        return len(nums)


a = Solution()
b = a.removeElement([1, 2, 3, 4, 5, 5, 5, 5], 5)
print(b)
