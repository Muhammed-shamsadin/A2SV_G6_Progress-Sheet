# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        res = []
        number = []
        
        c_code = 0
        for i in range(len(s)):
            if '@' in s and '.' in s:
                if s[i]  == "@":
                    d = s[i-1 :]
                    k = [s[0].lower(), "*****", d.lower()]
                    res.append("".join(k))
            else:
                if s[i].isdigit():
                    number.append(s[i])
        
        if len(number) == 10:
            last = "".join(number[6:])
            res.append("".join(["***-***-",last])) 
        elif len(number) == 11:
            last = "".join(number[7:])
            res.append("".join(["+*-***-***-",last])) 
        elif len(number) == 12:
            last = "".join(number[8:])
            res.append("".join(["+**-***-***-",last])) 
        elif len(number) == 13:
            last = "".join(number[9:])
            res.append("".join(["+***-***-***-",last])) 
        
        return res[0]

        

                




                




