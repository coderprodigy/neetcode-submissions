class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Brute force

        # initialize output string
        # intialize sublist in each loop
        # for every string in strs, store its frequencies in hashmap
        # iterate over other elements one by one
        # for each new string, compare the hashmap values of both strings, if match -> add it to that sublist
        # repeat till end


        # output = []
        # visited = set()

        # for i in range(len(strs)):

        #     if i in visited:
        #         continue

        #     freq_map = {}
        #     sublist = [strs[i]]
        #     visited.add(i)

        #     for x in strs[i]:

        #         freq_map[x] = freq_map.get(x,0) + 1

            
        #     for j in range(i+1, len(strs)):

        #         if j in visited:
        #             continue

        #         if len(strs[j]) != len(strs[i]):
        #             continue

        #         j_map = {}

        #         for x in strs[j]:

        #             j_map[x] = j_map.get(x,0) + 1
                
        #         #compare both hashmaps

        #         if freq_map == j_map:
        #             sublist.append(strs[j])
        #             visited.add(j)

        #     output.append(sublist)

        # return output


        # Hint 1 -> Brute Force 

        #Initialize a sorted_map = {}
        #key would be the sorted list and value would be a list of unsorted values
        #Iterate over all elements one by one.
        #Sort each string element, if it exists in hashmap, add the unsorted value to the list (value of key in hashmap)
        #finally after completing iteration -> create the output list, add append all values inside hashmap one by one.


        sorted_map = {}

        for i in range(len(strs)):

            sorted_key = "".join(sorted(strs[i]))

            if sorted_key in sorted_map:
                sorted_map[sorted_key].append(strs[i])
            
            else:
                sorted_map[sorted_key] = [strs[i]]

        
        output_list = []

        for x in sorted_map:

            output_list.append(sorted_map[x])
        

        return output_list





        








        