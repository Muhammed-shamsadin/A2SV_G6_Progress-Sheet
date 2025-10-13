class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)

        left = 0
        right = 0
        maxim = 0

        while right < len(s):
            while s[right] in count:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            count[s[right]] += 1
            maxim = max(maxim, right - left + 1)

            right += 1

        return maxim            
