class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for i in range(len(operations)):

            if operations[i]  == '+':
                current_ele = stack[-1] + stack[-2] #Doubt stack[-2] should not be allowed right?
                stack.append(current_ele)
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                current_ele = stack[-1] * 2
                stack.append(current_ele)
            else:
                stack.append(int(operations[i])) # stack.append(int(operations[i])) -> why I get error ValueError: invalid literal for int() with base 10: '+'
        
        sum = 0
        
        for j in range(0,len(stack)):

            sum += stack[j]

        return sum