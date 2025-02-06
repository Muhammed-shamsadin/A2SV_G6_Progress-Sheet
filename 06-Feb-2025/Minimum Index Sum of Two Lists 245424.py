# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        prev_idx = float('inf')

        idx_map = {}
        for i in range(len(list1)):
            idx_map[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in idx_map:
                curr_idx = i + idx_map[list2[i]]
                if curr_idx < prev_idx:
                    ans = [list2[i]]
                    prev_idx = curr_idx
                elif curr_idx == prev_idx:
                    ans.append(list2[i])
                    
        return ans