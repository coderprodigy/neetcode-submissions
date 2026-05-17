class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #My Brute force 1 thoughts - 

        #loop over s with i

        # loop over t with j to find s[i]

        # if I find s[i], replace t[j] with 1

        # else break and return false


        #Hint 1 -> Brute Force -> Sort both strings

        # sort both strings

        # compare both strings 

        # if same -> return true else return false

        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        if s_sorted == t_sorted:

            return True

        else:
            return False


        