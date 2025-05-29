class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def cus_log(log):
            left, right = log.split(" ", 1)

            if right[0].isalpha():
                return (0, right, left)

            else:
                return (1,)

        return sorted(logs, key = cus_log)
