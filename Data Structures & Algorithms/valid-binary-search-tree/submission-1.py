# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.arr = []
        self.res = True

    def DFS(self, current):
        if current is None:
            return

        if self.res == False:
            return

        self.DFS(current.left)

        if len(self.arr) > 0 and self.arr[-1] >= current.val:
            self.res = False
            return
        self.arr.append(current.val)

        self.DFS(current.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.DFS(root)
        return self.res
        