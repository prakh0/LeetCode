# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue =[root]
        max_level = 1
        max_sum = float("-inf")
        current_level = 1
        while queue: 
            level_sum = 0
            next_level = []
            for node in queue:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            queue = next_level
            current_level += 1
        return max_level
