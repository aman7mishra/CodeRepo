class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        s1 = [root]
        s2 = []
        level = []
        result = []
        while s1 or s2:
            while s1:
                current = s1.pop()
                level.append(current.val)
                if current.left:
                    s2.append(current.left)
                if current.right:
                    s2.append(current.right)
            result.append(level)
            level = []
            while s2:
                current = s2.pop()
                level.append(current.val)
                if current.right:
                    s1.append(current.right)
                if current.left:
                    s1.append(current.left)
            if level != []:
                result.append(level)
                level = []
        return result
                
