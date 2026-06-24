class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        length = len(nums) // 3
        output = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, values in count.items():
            if count[key] > length:
                output.append(key)
        return output
            
        