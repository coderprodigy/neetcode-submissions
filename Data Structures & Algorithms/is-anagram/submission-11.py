class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #My Brute force 1 thoughts - 

        #loop over s with i

        # loop over t with j to find s[i]

        # if I find s[i], replace t[j] with 1

        # else break and return false

        # t_list = list(t)

        # if len(s) != len(t):
        #     return False

        # for i in range(0,len(s)):

        #     if s[i] not in t_list:
        #         return False

        #     for j in range(0, len(t_list)):

        #         if s[i] == t_list[j]:
        #             t_list[j] = "1"
        #             break
            
        # return True





        #Hint 1 -> Brute Force -> Sort both strings

        # sort both strings

        # compare both strings 

        # if same -> return true else return false

        # s_sorted = "".join(sorted(s))
        # t_sorted = "".join(sorted(t))

        # if s_sorted == t_sorted:
        #     return True

        # else:
        #     return False

        # TC = O(nlogn + mlogm)
        # SC = O(1)



        # Hint 3 -> Hashmaps

        # compare the lengths of both strings

        # store the frequency of elements in hash table for each string

        # compare the hash table values one by one, if any mismatch return false

        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for x in s:

            if x in s_map:

                s_map[x] +=1

            else:
                s_map[x] = 1
        
        for x in t:

            if x in t_map:

                t_map[x] +=1

            else:
                t_map[x] = 1

        
        for x in s_map:

            if x not in t_map:
                return False

            elif s_map[x] != t_map[x]:
                return False
        

        return True




        
