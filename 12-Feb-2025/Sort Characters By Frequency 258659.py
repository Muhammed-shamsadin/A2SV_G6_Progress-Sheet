# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        # sorting dict based on key
        # reverse = dict(sorted(freq.items(), reverse = True))

        # sorting dict based on Value and reversing it
        rev_val = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True ))

        res = []
        for key, val in rev_val.items():
            new_char = key * val
            res.append(new_char)

        return ''.join(res)
        