class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        number_of_boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                number_of_boats += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                number_of_boats += 1
                right -= 1

        return number_of_boats



        