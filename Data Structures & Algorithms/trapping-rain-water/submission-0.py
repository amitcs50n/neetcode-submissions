class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        for i in range(len(height)):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])

            water_at_i = min(left_max, right_max) - height[i]
            total_water += water_at_i

        return total_water

        