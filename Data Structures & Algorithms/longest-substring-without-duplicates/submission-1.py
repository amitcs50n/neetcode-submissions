class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_length = 0
        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i, len(s)):
        #         if s[j] in seen:
        #             break
                
        #         seen.add(s[j])
        #         max_length = max(max_length, j - i + 1)
        
        # return max_length

        max_length = 0
        left = 0
        window = set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length, current_length)        
        return max_length



            
        

        