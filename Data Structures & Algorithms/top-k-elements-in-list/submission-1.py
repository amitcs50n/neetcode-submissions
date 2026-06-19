class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for num in nums:
            output[num] = output.get(num, 0) + 1
        
        result = []
        top_k = sorted(output, key=output.get, reverse=True)[:k]
        result.extend(top_k)

        return result


        