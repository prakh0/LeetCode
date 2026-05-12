# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTreeReverse(root.left, root.right)

    def isSameTreeReverse(self, i, j):
        if i is None and j is None:
            return True

        if i and j and i.val == j.val:
            return self.isSameTreeReverse(i.left, j.right) and self.isSameTreeReverse(i.right, j.left)

        return False