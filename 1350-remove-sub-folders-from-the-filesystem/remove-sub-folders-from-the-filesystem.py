class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        last_sub = None
        res = []
        for sub in folder:
            if last_sub is None or not sub.startswith(last_sub + '/'):
                res.append(sub)
                last_sub = sub

        return res