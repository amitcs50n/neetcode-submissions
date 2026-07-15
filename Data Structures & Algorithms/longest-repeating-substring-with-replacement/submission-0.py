class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_frequency = 0
        max_count = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        return max_count

            
        