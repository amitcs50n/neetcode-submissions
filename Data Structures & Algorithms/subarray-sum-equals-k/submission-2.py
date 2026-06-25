class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]

        #         if total == k:
        #             count += 1
        # return count

        #  now optimized sal..

        prefix_sum = 0
        count = 0
        prefix_count = {0:1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
            
        return count


