class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for subpath in path.split('/'):
            if subpath == '..':
                if stack:
                    stack.pop()
            elif not subpath or subpath == '.': 
                continue
            else:
                stack.append(subpath)


        return '/' + '/'.join(stack)