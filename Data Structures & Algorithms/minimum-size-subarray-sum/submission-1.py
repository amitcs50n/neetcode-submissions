class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # count = float("inf")
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         if total >= target:
        #             count = min(count, j - i + 1)
        #             break
        
        # return 0 if count == float("inf") else count

        count = float("inf")
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                count = min(count, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if count == float("inf") else count


        
        