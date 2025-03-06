class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        check = defaultdict(int)
        change = 0

        for num in bills:
            check[num] += 1
            change = num - 5
            if change == 0:
                continue
            elif change == 15:
                if check[5] >= 1 and check[10] >= 1:
                    check[5] -= 1
                    check[10] -= 1
                elif check[5] >= 3:
                    check[5] -= 3
                else:
                    return False
            elif check[change] > 0:
                check[change] -= 1
                
            else:
                return False
        
        return True