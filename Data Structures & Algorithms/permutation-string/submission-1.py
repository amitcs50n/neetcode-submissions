class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for i in range(len(s2) - len(s1) + 1):
        #     current = s2[i:i + len(s1)]

        #     if sorted(current) == sorted(s1):
        #         return True
        # return False

        if len(s1) > len(s2):
            return False
        
        required = {}
        window = {}
        left = 0

        for char in s1:
            required[char] = required.get(char, 0) + 1
        
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                left += 1
            
            if right - left + 1 == len(s1) and window == required:
                return True
        
        return False





        

        