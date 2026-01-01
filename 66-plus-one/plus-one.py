class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        to_str = ""

        for num in digits:
            to_str += str(num)
        
        plusOne = int(to_str) + 1
        to_str = str(plusOne)
        ans = []

        for char in to_str:
            ans.append(int(char))
        
        return ans