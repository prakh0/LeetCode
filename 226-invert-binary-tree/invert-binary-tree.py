# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return None
        if node.left is None and  node.right is None:
            return node
        right = self.invertTree(node.right)
        left = self.invertTree(node.left)
        node.right = left
        node.left = right
        return node