class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            total = 0
            count = 1
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    total = num
                    count += 1
            
            if count <= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer



        