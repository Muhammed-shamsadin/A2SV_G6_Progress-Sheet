# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0
        chars_count = Counter(chars)

        for i in range(len(words)):
            count = Counter(words[i])
            flag = True
            for letter in words[i]:
                if letter not in chars_count or count[letter] > chars_count[letter]:
                    flag = False
                    break
            if flag:
                answer += len(words[i])        

        return answer    
