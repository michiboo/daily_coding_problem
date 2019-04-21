'''A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''

class node():
    def __init__(self,val,r = None, l = None):
        self.val = val
        self.right = r
        self.left = l


def check(n,val):
    if n == None:
        return True
    r = True
    l = True
    if n.right:
        r = check(n.right,val)
    if n.left:
        l = check(n.left,val)
    
    if n.val == val:
        return True and r and l
    else:
        return False

def check1(root):
    count = 0
    stack = [root]
    while stack:
        root = stack.pop()
        if check(root,root.val):
            print('r',root.val)
            count += 1
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return count
    

a = node(0,node(1),node(0,node(1,node(1),node(1)),node(0)))

print(check1(a))







        