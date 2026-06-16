class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        result = []
        for i in strs:
            a = "".join(sorted(i))
            if a not in output:
                output[a]  = []

            output[a].append(i)
        
        for key, values in output.items():
            result.append(values)
        return result


            


        