class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

         #Brute Force -
         #Store <number> - <frequency> pair for each number in map
         #Iterate the map k number of times to find maximum frequency. Then enter that key in visited list
         #Return the visited list

        #Initialization
        visited = []
        freq_map = {}

        #Map population
        for x in nums:
            if  x in freq_map:
                freq_map[x]+=1
            else:
                freq_map[x]=1


        #Output population
        for i in range(k):

            max = 0
            max_value = -(1001)
            for val in freq_map:
                if freq_map[val] > max and val not in visited:
                    max = freq_map[val]
                    max_val = val

            visited.append(max_val)

        return visited

        
        

        