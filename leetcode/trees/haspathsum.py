class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        res = 0       
        def dfs(node):
            if not node: return 0
            nonlocal res
            res += node.val
            if node.left and dfs(node.left): return True
            if node.right and dfs(node.right): return True
            if not node.left and not node.right:
                if res == targetSum:
                    return True
            res -= node.val
                    
        return dfs(root)
