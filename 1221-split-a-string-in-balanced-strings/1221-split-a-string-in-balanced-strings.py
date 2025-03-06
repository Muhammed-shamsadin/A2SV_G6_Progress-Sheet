class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = Counter(s)
        max_substring = 0

        for char in s:
            count[char] -= 1

            if count["R"] == count["L"]:
                max_substring += 1
        
        return max_substring
