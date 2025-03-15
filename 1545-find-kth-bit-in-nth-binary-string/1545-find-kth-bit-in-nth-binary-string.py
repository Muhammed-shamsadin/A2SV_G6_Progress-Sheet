class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def solve(n):
            if n == 1:
                return '0'
                 
            prev = solve(n - 1)
            ans = []
            for c in prev:
                if c == '0':
                    ans.append('1')
                elif c == '1':
                    ans.append('0')

            ans.reverse()
            return prev + '1' + ''.join(ans)
        
        return solve(n)[k - 1]


