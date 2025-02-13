# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        k  = 0

        for i in range(n):
            maxim = max(arr[: n - i])
            k = arr.index(maxim) + 1
            
            arr[: k] = reversed(arr[ : k])
            res.append(k)

            arr[ : n - i] = reversed(arr[ : n - i])
            res.append(n - i)

        return res
