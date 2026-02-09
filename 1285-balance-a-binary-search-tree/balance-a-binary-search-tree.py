# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.result = []
        self.inorderTraversal(root)
        return self.BST(0,len(self.result) -1)
    def inorderTraversal(self,root):
        if not root:
            return
        self.inorderTraversal(root.left)
        self.result.append(root)
        self.inorderTraversal(root.right)
    def BST(self,left,right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = self.result[mid]
        root.left = self.BST(left,mid-1)
        root.right = self.BST(mid+1,right)
        return root