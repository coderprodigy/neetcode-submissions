class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        #Brute Force

        #Take 2 points i and j. Start i from left and j from right
        # run the loop till i < j
        #calculate sum at each point.
        # return [i,j]

        # i = 0
        # j = len(nums) - 1

        # while i<j:

        #     if nums[i] + nums[j] == target:
        #         return [i,j]
            
        #     else:
        #         i += 1
        #         j -= 1
        
        # return [i,j]

        
        #Brute Force version 2 -


        # for i in range(0,len(nums)):

        #     for j in range(i+1, len(nums)):

        #         if nums[i] + nums[j] == target:
        #             return [i,j]
                
        # TC - O(N^2) and SC - O(1)


        # Hint 2 and 3 -> hashmaps and difference approach

        #Optimized Solution

        # OInitialize a Hashmap of nums[i] -> index
        # Iterate over the array and keep checking if diff exists (Diff = Target - nums[i])
        # The moment we find a solution, return sorted indexes.

        index_map = {}
        for i in range(0,len(nums)):

            diff = target - nums[i]
            if diff in index_map:
                return sorted([i, index_map[diff]])
            
            else:
                index_map[nums[i]] = i



        