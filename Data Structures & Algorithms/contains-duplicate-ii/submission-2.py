class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False



        # window = []
        # for i in range(len(nums)):
        #     if nums[i] not in window:
        #         if i <= k - 1:
        #             window.append(nums[i])
        #         else:
        #             window.pop(0)
        #             window.append(nums[i])
        #     else:
        #         return True
            
        # return False



        window = set()
        left = 0
        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])
            if i - left >= k:
                window.remove(nums[left])
                left += 1
            
        return False


        



 






        