class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        # for i in range(len(height)):
        #     left_max = max(height[:i + 1])
        #     right_max = max(height[i:])

        #     water_at_i = min(left_max, right_max) - height[i]
        #     total_water += water_at_i

        # return total_water



        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water




        