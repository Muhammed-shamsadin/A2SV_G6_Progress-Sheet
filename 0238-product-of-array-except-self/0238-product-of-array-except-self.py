class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # optimized
        accumulate = []
        prod = 1
        # front
        for i in range(1, len(nums) + 1):
            accumulate.append(prod)
            prod = prod * nums[i - 1]

        prod = 1
        # back
        for i in range(len(nums) - 1, -1, -1):
            accumulate[i] *= prod
            prod *= nums[i]

        return accumulate

        # Better
        # length = len(nums)
        # res = [1] * (length)

        # prefix = 1
        # for i in range(length):
        #     res[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for i in range(length - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]

        # return res