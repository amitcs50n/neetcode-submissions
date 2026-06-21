class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     total = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             total *= nums[j]
        #     output.append(total)

        # return output

        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]

        return output





        