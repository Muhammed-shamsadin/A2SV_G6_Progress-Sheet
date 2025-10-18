class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
            elif (ch == ")" and stack[-1] == "(") or (ch == "}" and stack[-1] == "{") or (ch == "]" and stack[-1] == "["):
                stack.pop()
            else:
                stack.append(ch)
        
        if stack:
            return False
        
        return True
