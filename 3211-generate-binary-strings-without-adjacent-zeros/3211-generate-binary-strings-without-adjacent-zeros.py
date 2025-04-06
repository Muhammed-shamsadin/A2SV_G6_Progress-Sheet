class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def generate(curr):
            # base case
            if len(curr) == n:
                ans.append(''.join(curr))
                return
            
            curr.append("1")
            generate(curr)
            curr.pop()

            if curr[-1] == "1":
                curr.append("0")
                generate(curr)
                curr.pop()
        

        generate(["0"])
        generate(["1"])
        return ans

