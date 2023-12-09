# # Challenge Context
# Given the root of a binary tree, construct a string consisting of parenthesis and
# integers from a binary tree with the preorder traversal way, and return it.
# Challenge Link --> https://leetcode.com/problems/construct-string-from-binary-tree/?envType=daily-question&envId=2023-12-08


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode], otp="") -> str:
        if root:
            otp += str(root.val)
            if root.left:
                otp += "("
                otp = self.tree2str(root.left, otp)
                otp += ")"
            if not root.left and root.right:
                otp += "()"
            if root.right:
                otp += "("
                otp = self.tree2str(root.right, otp)
                otp += ")"
        return otp
