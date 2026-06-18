class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = {}
        # for i in nums:
        #     count[i] = count.get(i,0) + 1

        # index = 0

        # for _ in range(count.get(0, 0)):
        #     nums[index] = 0
        #     index += 1
        
        # for _ in range(count.get(1, 0)):
        #     nums[index] = 1
        #     index += 1
        
        # for _ in range(count.get(2, 0)):
        #     nums[index] = 2
        #     index += 1

        #   this is one way to dop this

        left = 0
        current = 0
        right = len(nums) - 1

        while current <= right:
            if nums[current] == 0:
                temp = nums[left]
                nums[left] = nums[current]
                nums[current] = temp
                left += 1
                current += 1
            
            elif nums[current] == 2:
                temp = nums[right]
                nums[right] = nums[current]
                nums[current] = temp
                right -= 1

            else:
                current += 1





        
            
        

            

        