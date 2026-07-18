class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = sorted(
            arr, key=lambda num: (abs(num - x), num))[:k]
        
        return sorted(closest)

        