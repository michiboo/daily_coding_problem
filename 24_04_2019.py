'''Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'        
        
        '''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(n):
    tmp = str(n.val) 
    stack = [n]
    lc = 1
    rc = 1
    while stack:
        tn = stack.pop()
        if tn.left:
            stack.append(tn.left)
            tmp = tmp + '*' + lc * 'L'+'*' + str(tn.left.val)
        if tn.right:
            stack.append(tn.right)
            tmp = tmp + '*' + rc * 'R'+'*' + str(tn.right.val)
    return tmp
#not finish
def deserialize(s):
    s = [i for i in s.split('*')]
    root = Node(s[0])


node = Node('root', Node('left', Node('left.left')), Node('right'))
s = serialize(node)
print(serialize(node))
deserialize(s)