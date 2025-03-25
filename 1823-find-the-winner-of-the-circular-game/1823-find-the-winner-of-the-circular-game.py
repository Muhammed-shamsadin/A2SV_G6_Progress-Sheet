class Solution:
    def findTheWinner(self, n: int, k: int) -> int:        
        arr = []
        eliminate = 0
        for i in range(1, n + 1):
            arr.append(i)

        def find(eliminate):
            if len(arr) == 1:
                return 

            eliminate = (eliminate + k - 1) % len(arr)
            arr.pop(eliminate)
            find(eliminate)
        
        find(0)
        return arr[0]