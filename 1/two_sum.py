from typing import List

# This solution has a time complexity of O(n), since we only need to 
# traverse the list once, keeping track of the numbers we have seen in our map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        merp = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in merp:
                return [merp[diff], i]
            merp[num] = i
