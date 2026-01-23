# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, node: Optional[TreeNode]) -> TreeNode:
        if node == None or node.left == None and node.right == None:
            return node

        last_left = self.flatten(node.left)
        last_right = self.flatten(node.right)

        if last_left != None:
            last_left.right = node.right
            node.right = node.left
        node.left = None
        
        if last_right == None:
            last_right = last_left
        
        return last_right
        
        
        