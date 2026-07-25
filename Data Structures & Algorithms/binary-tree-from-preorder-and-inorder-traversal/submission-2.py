# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #we have two trees pre order and inorder
        # the main part about thsi is that pre order gives the first root
        # the inorder gives the left side of the index and the right side. from then on 
        # we can efficivelty tell which one is the left and right for that root and recurse

        if not preorder and not inorder:
            return
        root = TreeNode(preorder[0])
        # have the first root set up here
        # thinking of finding the index in inorder and then identifying the others
        mid = inorder.index(preorder[0])
        # left side of inporder is to the left and right side is to the right o fmid
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
        return root

        



        


        