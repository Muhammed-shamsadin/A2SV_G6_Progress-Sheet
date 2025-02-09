# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        '''
            scene
        '''
        dic = {1: 'I', 90: 'XC', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 
                100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        
        # sort and reverse dictionary, so that we iterate in descending manner
        reversed_dic = dict(sorted(dic.items(), reverse=True))

        res = ""
        for value, symbol in reversed_dic.items():
            if num // value:
                # number of times, we add the symbol
                times = num // value
                res += (symbol * times)

                num = num % value
        
        return res

