# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        order = {1:"qwertyuiop", 2:"asdfghjkl", 3:"zxcvbnm"}
        res = []

        for word in words:
            found = 0
            first_letter = word[0].lower()

            # hold the key or the row of the first letter
            for key in order:
                if first_letter in order[key]:
                    found =  key
                    break

            # for each letter check them if they are found in the related key of the 1st letter
            flag = True
            for letter in word.lower():
                if letter not in order[found]:
                    flag = False
                    break

            if flag:
                res.append(word)
            
        return res