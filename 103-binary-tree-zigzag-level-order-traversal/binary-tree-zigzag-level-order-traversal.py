# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        from_left = True
        while queue:
            level_size = len(queue)
            level_node = []
            for _ in range(level_size):
                node = queue.popleft()
                if from_left:
                    level_node.append(node.val)
                else:
                    level_node.insert(0,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_node)
            from_left = not from_left
        return result