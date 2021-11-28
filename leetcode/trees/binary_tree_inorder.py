def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
     if root is None:
         return []
     result_array = []
     def traverse_rec(node):
     if node.left:
         traverse_rec(node.left)
     result_array.append(node.val)
     if node.right: 
         traverse_rec(node.right)
     traverse_rec(root)
     return result_array
                          
