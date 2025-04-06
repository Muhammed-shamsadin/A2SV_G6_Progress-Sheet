class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = ["1"]
        count = 2
        ans = []

        for i in range(len(pattern)):
            while stack and pattern[i] == 'I':
                ans.append(stack.pop())
            
            stack.append(str(count))
            count += 1
        
        while stack:
            ans.append(stack.pop())

        return ''.join(ans)