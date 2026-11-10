class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        

        for brac in s:

            if brac == '{' or brac == '[' or brac == '(':
                stack.append(brac)
            

            else:
                if brac == ')':
                    if len(stack)!=0 and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if brac == '}':
                    if len(stack)!=0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if brac == ']':
                    if len(stack)!=0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            
        if len(stack) == 0:
            return True
        
        else:
            return False



        