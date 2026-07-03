# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#         total = []
#         for i in operations:
#             if i.isdigit():
#                 total.append(int(i))
#             elif i == "+":
#                 total.append(sum(total[-2:]))
#             elif i == "C":
#                 total.pop()
#             elif i == "D":
#                 total.append(2*total[-1])
            
#         return sum(total)


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []

        for i in operations:
            if i == "+":
                total.append(total[-1] + total[-2])
            elif i == "C":
                total.pop()
            elif i == "D":
                total.append(2 * total[-1])
            else:
                total.append(int(i))

        return sum(total)

        