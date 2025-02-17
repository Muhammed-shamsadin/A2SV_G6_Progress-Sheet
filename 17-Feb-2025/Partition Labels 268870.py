# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = defaultdict(int)
        for i, char in enumerate(s):
            index[char] = i
            
        res = []
        max_idx = 0
        left = 0
        for right in range(len(s)):
            max_idx = max(max_idx, index[s[right]])

            if right == max_idx:
                res.append(right - left + 1)
                max_idx = right + 1
                left = max_idx
        
        return res
            