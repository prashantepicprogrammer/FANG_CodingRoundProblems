class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def min_depth_bst(root):
    if root is None :
        return 0 
    
    if root.left is None and root.right is None :
        return 1 
    
    if root.left is None :
        return min_depth_bst(root.right) + 1 
    
    if root.right is None :
        return min_depth_bst(root.left) + 1
    
    return min(min_depth_bst(root.left) , min_depth_bst(root.right)) + 1

  
n3 = Node(3, None, Node(4))
n2 = Node(2 )
n1 = Node(1, n2, n3)

#     1
#    / \
# +1 2   3 +1
#        \      +2
#         4 +1 
print(min_depth_bst(n1)) # 2 