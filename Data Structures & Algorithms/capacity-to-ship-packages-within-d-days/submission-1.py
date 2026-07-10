class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            used_day = 1
            current_load  = 0
            for weight in weights:
                if current_load  + weight > mid:
                    used_day += 1
                    current_load  = 0

                current_load  += weight
            
            if used_day <= days:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
        






                








        