# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for word in strs:
            sort_word = sorted(word)
            sort_word = ''.join(sort_word)
            count[sort_word].append(word)

        return list(count.values())

