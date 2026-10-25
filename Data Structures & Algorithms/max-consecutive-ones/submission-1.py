import math

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_count = 0
        current_count = 0

        for index in range(0, len(nums)):

            if nums[index] ==1:
                current_count +=1
                if max_count <current_count:
                    max_count = current_count

            elif nums[index] != 1:
                current_count=0

        return max_count        