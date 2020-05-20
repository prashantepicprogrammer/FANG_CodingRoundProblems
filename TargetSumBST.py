"""Given a binary tree, and a target number, find if there is a path from the root to any leaf that sums up to the target.
"""

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def target_sum_bst(root, target):

    if root is not None :
        result = bool() # False 
        new_target = target - root.value

        if new_target == 0 and root.left == None and root.right == None :
            return True 

        if root.left is not None :
            if target_sum_bst(root.left, new_target) or result :
                result = True
        
        if root.right is not None :
            if target_sum_bst(root.right, new_target) or result :
                result = True
        return result

#      1
#    /   \
#   2     3
#    \     \
#     6     4
n6 = Node(6)
n4 = Node(4)
n3 = Node(3, None, n4)
n2 = Node(2, None, n6)
n1 = Node(1, n2, n3)

print(target_sum_bst(n1, 5))