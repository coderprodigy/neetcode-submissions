class Solution:
    def isValid(self, s: str) -> bool:

        length = len(s)
        
        if length %2 !=0:
            return False


        operations = []

        for br in s:

            if br == '(' or br == '{' or br == "[":
                operations.append(br)

            elif br ==")":
                if len(operations)!=0 and operations[-1] == "(" :
                    operations.pop()
                    continue 
                elif len(operations)==0 or operations[-1] != "(" :
                    return False
            
            elif br =="}":
                if len(operations)!=0 and operations[-1] == "{":
                    operations.pop()
                    continue 
                elif len(operations)==0 or operations[-1] != "{" :
                    return False

            elif br =="]":
                if len(operations)!=0 and operations[-1] == "[":
                    operations.pop()
                    continue 
                elif len(operations) ==0 or operations[-1] != "[" :
                    return False

        if len(operations) == 0:
            return True
        else:
            return False
            









        

        


        