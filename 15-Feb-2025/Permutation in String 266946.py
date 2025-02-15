# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target_counter = Counter(s1)
        left = 0
        right = len(s1)
        window = Counter(s2[:len(s1)])
        
        if window == target_counter:
            return True

        while right < len(s2):
            window[s2[right]] += 1
            window[s2[left]] -= 1

            if window == target_counter:
                return True
            right += 1
            left += 1

        return False
