class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # output = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             output[i] = j - i
        #             break
        # return output

        stack = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, val = stack.pop()
                output[index] = i - index
            stack.append((i, temp))

        return output



                


        