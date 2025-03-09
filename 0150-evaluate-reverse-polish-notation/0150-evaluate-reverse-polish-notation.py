class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        length = len(tokens)

        for i in range(length):
            if tokens[i] == '+':
                pop1 = stack.pop()
                pop2 = stack.pop()
                val = int(pop1) + int(pop2)
                stack.append(val)
            elif tokens[i] == '*':
                pop1 = stack.pop()
                pop2 = stack.pop()
                val = int(pop1) * int(pop2)
                stack.append(val)
            elif tokens[i] == '/':
                pop1 = stack.pop()
                pop2 = stack.pop()
                val = int(pop2) / int(pop1)
                if val < 0:
                    val = math.ceil(val)
                else:
                    val = math.floor(val)
                stack.append(val)                
            elif tokens[i] == '-': 
                pop1 = stack.pop()
                pop2 = stack.pop()
                val = int(pop2) - int(pop1)
                stack.append(val) 
            else:
                stack.append(tokens[i])

        return int(stack[0])