class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex - 1)

        curr = [1]
        n = len(prev)
        for i in range(n - 1):
            curr.append(prev[i] + prev[i + 1])
        curr.append(1)

        return curr


        