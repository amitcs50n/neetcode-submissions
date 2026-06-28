class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:] = list(dict.fromkeys(nums))
        # k = len(nums)
        # return k

        i = 0
        while i < len(nums):
            if nums.count(nums[i]) > 1:
                nums.pop(i)
            else:
                i +=1
        return i


        