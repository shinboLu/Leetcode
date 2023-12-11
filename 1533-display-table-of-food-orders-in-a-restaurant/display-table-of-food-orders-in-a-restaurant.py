class Solution:
    def find_table(self, table, res):
        for i in range(len(res)):
            if res[i][0] == table:
                return i
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_set = set()
        dish_set = set()
        #print(table_set, dish_set)
        for order in orders:
            table_set.add(order[1])
            dish_set.add(order[2])

        sorted_table = [int(x) for x in table_set]
        sorted_table.sort()

        sorted_dish = [x for x in dish_set]
        sorted_dish.sort()
        
        res = [[0] * (len(dish_set)+1) for _ in range(len(table_set)+1)]

        res[0][1:] = sorted_dish

        for i in range(1, len(sorted_table)+1):
            res[i][0] = str(sorted_table[i-1])

        for order in orders:
            table = order[1]
            dish = order[2]

            dish_index = res[0].index(dish)
            table_index = self.find_table(table, res)
            res[table_index][dish_index] += 1
        
        
        for row in range(len(res)):
            for col in range(len(res[0])):
                res[row][col] = str(res[row][col])

        res[0][0] = 'Table'
        return res 
                


        



        
