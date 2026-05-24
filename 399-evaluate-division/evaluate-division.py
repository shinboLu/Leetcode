class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = collections.defaultdict(lambda: collections.defaultdict(float))
        for (divd, divsr), value in zip(equations, values):
            adj_list[divd][divsr] = value
            adj_list[divsr][divd] = 1/value


        def bt_eval(cur_node, target_node, acc_prod, visited): 
            visited.add(cur_node)
            ret = -1.0 
            neis = adj_list[cur_node]

            if target_node in neis:
                ret = acc_prod * neis[target_node] 
            else:
                for nei, val in neis.items():
                    if nei in visited:
                        continue
                    ret = bt_eval(nei, target_node, acc_prod * val, visited)

                    if ret != -1.0:
                        break
            visited.remove(cur_node)
            return ret
        res = []
        for divd, divr in queries:
            if divd not in adj_list or divr not in adj_list:
                ret = -1.0
            elif divd == divr: 
                ret = 1.0
            else:
                visited = set() 
                ret = bt_eval(divd, divr, 1, visited)
            res.append(ret)
        return res

        