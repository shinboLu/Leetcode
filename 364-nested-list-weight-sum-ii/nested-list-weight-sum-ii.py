# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth=float('-inf')
        res = 0 
        def dfs_get_max_depth(nest_list, cur_depth):
            nonlocal max_depth
            for sub_list in nest_list:
                if sub_list.isInteger():
                    max_depth = max(max_depth, cur_depth)
                else:
                    dfs_get_max_depth(sub_list.getList(), cur_depth+1)
        dfs_get_max_depth(nestedList, 1)

        def dfs_get_sum(nest_list, cur_depth):
            nonlocal max_depth, res
            for sub_list in nest_list:
                if sub_list.isInteger():
                    res+=sub_list.getInteger()* (max_depth-cur_depth+1)
                else:
                    dfs_get_sum(sub_list.getList(), cur_depth+1)

        dfs_get_sum(nestedList, 1)
        return res

