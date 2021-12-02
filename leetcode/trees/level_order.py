class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root:
            queue = [root]
            while len(queue) > 0:
                level = []
                for i in range(len(queue)):
                    current = queue.pop(0)
                    level.append(current.val)
                    if current.left: queue.append(current.left)
                    if current.right: queue.append(current.right)
                result.append(level)
            
        return result
