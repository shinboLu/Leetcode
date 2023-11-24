class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
# You want to make an adj list containing those who are richer.
# Then from those people in the list you want to recursively find the min quiet value.
# Make sure to have a default min val which is quiet[i] as there are times where adj_list[i] is an empty array.
        n = len(quiet)
        adj_list = collections.defaultdict(list)
        for richer_person, rich_person in richer:
            adj_list[rich_person].append(richer_person)
        memoization = [None] * n

        def dfs(idx, memoization):
            if memoization[idx] is not None:
                return memoization[idx]
            
            result = (quiet[idx], idx)
            for next_idx in adj_list[idx]:
                more = dfs(next_idx, memoization)
                if more[0] < result[0]:
                    result = more
            memoization[idx] = result
            return result 
        for idx in range(n):
            dfs(idx, memoization)

        return [idx for _, idx in memoization]
                







