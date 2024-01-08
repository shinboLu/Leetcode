class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Build array rank where rank[i][j] is the number of votes for team i to be the j-th rank.
        # Sort the trams by rank array. if rank array is the same for two or more teams, sort them by the ID in ascending order.

        rank = collections.defaultdict(list)

        for vote in votes:
            for idx, team in enumerate(vote):
                if team not in rank:
                    rank[team] = [0] * len(vote)
                rank[team][idx] += 1
        
        #voted_names = sorted()
        print(rank.items())

        ranked_team = sorted(rank.keys())

        return ''.join(sorted(ranked_team, key = lambda x:rank[x], reverse = True))
