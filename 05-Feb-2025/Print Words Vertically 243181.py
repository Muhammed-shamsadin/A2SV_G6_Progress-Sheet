# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()

        max_length = max(len(i) for i in s)
        answer = []
        
        for i in range(max_length):
            res = ""
            for word in s:
                if i < len(word):
                    res += word[i]
                else:
                    res += " "
            # print(res)
            answer.append(res.rstrip())
        
        return answer
        
            