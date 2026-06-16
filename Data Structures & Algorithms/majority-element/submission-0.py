class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums) // 2
        
        for i in nums:
            count[i] = count.get(i, 0) + 1

        for key, value in count.items():
            if value > n:
                return key



        