class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = ['']
        max_len = 0

        for i in range(len(arr)):
            for j in range(len(unique)):
                temp = arr[i] + unique[j]
                if len(temp) == len(set(temp)):
                    unique.append(temp)
                    max_len = max(max_len, len(temp))

        return max_len
