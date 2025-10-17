class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == ']':
                text = []
                while stack and stack[-1] != '[':
                    text.append(stack.pop())
                stack.pop()

                text.reverse()
                text = ''.join(text)
            
                digit = []
                while stack and stack[-1].isdigit():
                    digit.append(stack.pop())
                digit.reverse()

                digit = int(''.join(digit))
                stack.append(digit * text)

            else:
                stack.append(s[i])
        
        return ''.join(stack)
        

                