class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # keep count for both s and t
        freq_s = Counter(s)
        freq_t = Counter(t)

        if len(s) !=  len(t):
            return False

        # check if all character are in t and there count are equal
        for char in t:
            if char not in s or freq_s[char] != freq_t[char]:
                return False
        
        return True