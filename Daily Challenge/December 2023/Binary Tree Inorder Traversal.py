# # Challenge Context
# GGiven the root of a binary tree, return the inorder traversal of its nodes' values.
# Challenge Link --> https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=daily-question&envId=2023-12-09


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], output=None) -> List[int]:
        if not output:
            output = []
        if root:
            if root.left:
                output = self.inorderTraversal(root.left, output)

            output.append(root.val)

            if root.right:
                output = self.inorderTraversal(root.right, output)
        return output
