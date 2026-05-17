class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        map = {}

        for ele in nums:

            if ele in map:
                return True
            
            else:
                map[ele] = 1
        
        return False



        