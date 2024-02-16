class Solution:
    def isValid(self, s: str) -> bool:
        s_list = [x for x in s]
        stack = []

        for paran in s_list:
            if paran in ('(', '{', '['):
                stack.append(paran)
            if paran in (')', '}', ']'):
                if len(stack) != 0:
                    left_paran = stack.pop()
                    if paran == ')' and left_paran == '(':
                        continue
                    elif paran == '}' and left_paran == '{':
                        continue
                    elif paran == ']' and left_paran == '[':
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False 
        return True


        