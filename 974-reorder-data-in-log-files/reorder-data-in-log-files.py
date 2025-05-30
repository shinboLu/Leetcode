class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def hasNum(log):
            return any(char.isdigit() for char in log)

        letter_log = []
        digit_log = []
        for i,log in enumerate(logs):
            splits = log.split(' ')
            if hasNum(splits[1:]):
                digit_log.append(log)
            else:
                letter_log.append([' '.join(splits[1:]), splits[0], i])
        res = []
        for log in sorted(letter_log):
            res.append(logs[log[2]])



        return res + digit_log