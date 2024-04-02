class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_lim = float('-inf')

        stack = []

        for num in preorder:
            #print(num, stack)
            while stack and stack[-1] < num:
                min_lim = stack.pop() 

            if num <= min_lim:
                return False 

            stack.append(num)

        return True            
            