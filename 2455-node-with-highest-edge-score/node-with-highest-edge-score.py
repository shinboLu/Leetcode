class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        array = [0] * len(edges)
        for num, index in enumerate(edges):
            array[index] += num
        return array.index(max(array))


        
        