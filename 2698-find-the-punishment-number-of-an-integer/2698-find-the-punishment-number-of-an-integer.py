class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def check(index,target,s):
            
            if index >= len(s):
                if target == 0:
                    return True
                return False
            
            for i in range(index + 1, len(s)+1):
                cur = int(s[index:i]) if s[index:i] != "" else 0
                if check(i,target-cur,s):
                    return True
            
            return False
            
        
        answer = 0
        for num in range(1,n+1):
            square_number = num**2
            if check(0,num,str(square_number)):
                print(num)
                answer += square_number
        
        return answer
