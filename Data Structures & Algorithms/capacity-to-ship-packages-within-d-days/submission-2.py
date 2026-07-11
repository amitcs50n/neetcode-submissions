class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            current_weight = 0
            count_days = 1

            for weight in weights:
                if current_weight + weight <= mid:
                    current_weight += weight
                else:
                    count_days += 1
                    current_weight = weight

            if count_days <= days:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
        






                








        