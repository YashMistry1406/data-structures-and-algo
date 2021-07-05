#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1g3ZW1jVGVvdnBES2JYX0xpVWlheElqYWFGUXxBQ3Jtc0tuRGhtWW9oYk9Jc3hHMXo3SFdXUUMxejZvMFlFUW95SHB1SDYtYXV1VFVOLWk3Qmx5R093anJremNTZGhndUctQVhEM1RmQUJNaWQ2bGlwRlp0S1dGM24xcHc0Ukg4b1NiSEM0T0pmVVBxa1Y2LTdtYw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fpartition-problem-dp-18%2F
class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        sum = 0
        i, j = 0, 0
        n = len(arr)

        # calculate sum of all elements
        for i in range(n):
            sum += arr[i]

        if sum % 2 != 0:
            return False

        part = [[True for i in range(n + 1)]
                for j in range(sum // 2 + 1)]

        # initialize top row as true
        for i in range(0, n + 1):
            part[0][i] = True

        # initialize leftmost column,
        # except part[0][0], as 0
        for i in range(1, sum // 2 + 1):
            part[i][0] = False

        # fill the partition table in
        # bottom up manner
        for i in range(1, sum // 2 + 1):

            for j in range(1, n + 1):
                part[i][j] = part[i][j - 1]

                if i >= arr[j - 1]:
                    part[i][j] = (part[i][j] or
                                  part[i - arr[j - 1]][j - 1])

        return part[sum // 2][n]
