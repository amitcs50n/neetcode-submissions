class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            used_day = 1
            total_weight_can_carry_in_a_day = 0
            for weight in weights:
                if total_weight_can_carry_in_a_day + weight > mid:
                    used_day += 1
                    total_weight_can_carry_in_a_day = 0

                total_weight_can_carry_in_a_day += weight
            
            if used_day <= days:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
        






                








        