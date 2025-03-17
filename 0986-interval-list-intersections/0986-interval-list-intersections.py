class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        pref_dict = defaultdict(int)

        for start, end in firstList:
            pref_dict[start] += 1
            pref_dict[end + 1] -= 1
        
        for start, end in secondList:
            pref_dict[start] += 1
            pref_dict[end + 1] -= 1
        
        sorted_key = sorted(pref_dict.keys())
        
        res = []
        curr_sum = 0
        prev = None
        for key in sorted_key:
            if curr_sum == 2:
                res.append([prev, key - 1])
            
            curr_sum += pref_dict[key]
            prev = key
        
        return res