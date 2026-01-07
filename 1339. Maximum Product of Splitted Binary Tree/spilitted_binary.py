# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_product = 0
            
        def findTotalSum(node):
            if node is None:
                return 0
                
            left_sum = findTotalSum(node.left)
            right_sum = findTotalSum(node.right)
                
            return node.val + left_sum + right_sum
            
        total_sum = findTotalSum(root)
            
        def findSubtreeSum(node):
            if node is None:
                return 0
                
            left_sum = findSubtreeSum(node.left)
            right_sum = findSubtreeSum(node.right)
                
            subtree_sum = node.val + left_sum + right_sum
                
            product = subtree_sum * (total_sum - subtree_sum)
                
            if product > self.max_product:
                self.max_product = product
                
            return subtree_sum
            
        findSubtreeSum(root)
            
        return self.max_product % MOD