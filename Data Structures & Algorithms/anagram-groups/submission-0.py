class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Brute force

        # initialize output string
        # intialize sublist in each loop
        # for every string in strs, store its frequencies in hashmap
        # iterate over other elements one by one
        # for each new string, compare the hashmap values of both strings, if match -> add it to that sublist
        # repeat till end


        output = []
        visited = set()

        for i in range(len(strs)):

            if i in visited:
                continue

            freq_map = {}
            sublist = [strs[i]]
            visited.add(i)

            for x in strs[i]:

                freq_map[x] = freq_map.get(x,0) + 1

            
            for j in range(i+1, len(strs)):

                if j in visited:
                    continue

                if len(strs[j]) != len(strs[i]):
                    continue

                j_map = {}

                for x in strs[j]:

                    j_map[x] = j_map.get(x,0) + 1
                
                #compare both hashmaps

                if freq_map == j_map:
                    sublist.append(strs[j])
                    visited.add(j)

            output.append(sublist)

        return output






        