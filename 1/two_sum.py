from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        merp = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in merp:
                return [merp[diff], i]
            merp[num] = i
