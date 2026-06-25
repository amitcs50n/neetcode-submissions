class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = 1
        while True:
            if x not in nums:
                return x
            x += 1

        