class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num_list_1 = []
        num_list_2 = []
        num_list_target = []

        for word in firstWord:
            val = ord(word) - ord('a')
            num_list_1.append(str(val))

        for word in secondWord:
            val = ord(word) - ord('a')
            num_list_2.append(str(val))

        for word in targetWord:
            val = ord(word) - ord('a')
            num_list_target.append(str(val))

        print(''.join(num_list_1))
        num1 = int(''.join(num_list_1))
        num2 = int(''.join(num_list_2))
        tar_num = int(''.join(num_list_target))

        return True if num1 + num2 == tar_num else False