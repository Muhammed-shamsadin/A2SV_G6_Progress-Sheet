class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        
        cmn_elt = count.most_common(k)
        
        result = []
        for element in cmn_elt:
            num = element[0]  
            result.append(num)
        
        return result
