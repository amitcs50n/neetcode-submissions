class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, value in enumerate(nums):
            number = target - value
            if number in result:
                return [result[number], i]
            result[value] = i

           
            

            

            