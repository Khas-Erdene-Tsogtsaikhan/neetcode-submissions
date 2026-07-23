# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = [] 
        # intiialize the list over herre

        def dfs(root, n):
            if not root:
                return 
            if len(res) == n:
                res.append([])
            # this makes sure that we can actually track the levels for each lebel of the tree
            res[n].append(root.val)
            dfs(root.left, n+1)
            dfs(root.right, n+1)
        dfs(root, 0)
        return res

        