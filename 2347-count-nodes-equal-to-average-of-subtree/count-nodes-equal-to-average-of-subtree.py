# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def dfs(self, node):
        if not node:
            return 0,0
        left_sum, left_count = self.dfs(node.left)
        right_sum, right_count = self.dfs(node.right)

        total_sum = left_sum +right_sum + node.val
        total_count = left_count + right_count +1

        if total_sum // total_count == node.val:
           self.count += 1
        return total_sum, total_count
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.count
       


        