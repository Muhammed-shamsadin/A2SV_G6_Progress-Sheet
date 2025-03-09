class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        count = 0
        for char in s:
            if char == ")":
                while stack and stack[-1] == "(":
                    stack.pop()
                    count += 1
            else:
                stack.append(char)
        
        return count


