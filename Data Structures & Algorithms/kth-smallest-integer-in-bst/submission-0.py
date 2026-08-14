# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = None
        self.k = 0

    def DFS(self, current, k):
        if current is None:
            return

        if self.res is not None:
            return

        self.DFS(current.left, k)

        self.k += 1
        if self.k == k:
            self.res = current.val
            return
        
        self.DFS(current.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.DFS(root, k)
        return self.res
        