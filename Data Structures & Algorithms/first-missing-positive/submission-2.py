class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # x = 1
        # while True:
        #     if x not in nums:
        #         return x
        #     x += 1
        

        # s = set(nums)
        # x = 1
        # while x in nums:
        #     x += 1
        # return x

        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

         
        