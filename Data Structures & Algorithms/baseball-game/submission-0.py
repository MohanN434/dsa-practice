class Solution:
    def calPoints(self, operations: List[str]) -> int:
        totalRecord = []

        for i in range(len(operations)):
            if operations[i] == '+':
                totalRecord.append(int(totalRecord[-1]) + int(totalRecord[-2]))
            elif operations[i] == 'C':
                totalRecord.pop()
            elif operations[i] == 'D':
                totalRecord.append(int(totalRecord[-1]) * 2)
            else:
                totalRecord.append(int(operations[i]))

        return sum(totalRecord)