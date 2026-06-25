class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # x = 1
        # while True:
        #     if x not in nums:
        #         return x
        #     x += 1
        
        s = set(nums)
        x = 1
        while x in nums:
            x += 1
        return x
         
        