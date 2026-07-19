class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        for i in range(len(nums)):
            window_size = i - left + 1

            if window_size == k:
                result.append(max(nums[left:i + 1]))
                left += 1
            
        return result


        