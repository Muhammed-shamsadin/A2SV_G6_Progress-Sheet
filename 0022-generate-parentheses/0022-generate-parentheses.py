class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(curr, open, total_opened):
            if len(curr) == 2*n:
                if open == 0:
                    ans.append(''.join(curr))
                return
            
            # do for when it is opened
            if total_opened < n:
                curr.append("(")
                generate(curr, open + 1, total_opened + 1)
                curr.pop()

            if open > 0:
                curr.append(")")
                generate(curr, open - 1, total_opened)
                curr.pop()
        
        generate(["("], 1, 1)

        return ans