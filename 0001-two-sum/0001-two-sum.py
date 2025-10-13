class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        answer = []

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict:
                answer.append(my_dict[diff])
                answer.append(i) 

            my_dict[nums[i]] = i
        
        return answer

        
            
            
