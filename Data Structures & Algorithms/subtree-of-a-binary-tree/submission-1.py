# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #traversal throughout the root, if the root is the same value as the subroot
        #then comapre directly
        # have a seaprate function for cpomparing
        #base case should be that if subroot is null as well as the root
        if not subRoot:
            return True
        if not root:
            return False
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot:
                if root.val == subRoot.val:
                    return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
            else:
                return False

        if root.val == subRoot.val:
            if sameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                    

        



        

        