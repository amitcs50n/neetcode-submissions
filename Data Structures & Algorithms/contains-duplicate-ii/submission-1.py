class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False

        store = {}
        for index, value in enumerate(nums):
            if value not in store:
                store[value] = index
            else:
                if abs(store[value] - index) <= k:

                    return True
                store[value] = index
            
        return False






        