class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Example use of Node
x = Node("A")
x.left = Node("B")
x.right = Node("C")
x.left.left = Node("D")
x.left.right = Node("E")
x.right.left = Node("F")

def dfs_preoder_recursive(root):
    def dfs(node, res):
        if not node:
            return 
        res.append(node.val)
        dfs(node.left, res)
        dfs(node.right, res)
    res = []
    dfs(root, res)
    return res

dfs_preoder_recursive(x)

def dfs_preoder_iterative(root):
    if not root:
        return []
    
    res = []
    stack = [root]

    while stack:
        ref = stack.pop()
        res.append(ref.val)

        if ref.right:
            stack.append(ref.right)
        if ref.left:
            stack.append(ref.left)
    
    return res

dfs_preoder_iterative(x)

def dfs_inoder_recursive(root):
    def dfs(node, res):
        if not node:
            return 
        dfs(node.left, res)
        res.append(node.val)
        dfs(node.right, res)
    res = []
    dfs(root, res)
    return res

dfs_inoder_recursive(x)

def dfs_inoder_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process the node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result

dfs_inoder_iterative(x)

def dfs_postoder_recursive(root):
    def dfs(node, res):
        if not node:
            return
        dfs(node.left, res)
        dfs(node.right, res)
        res.append(node.val)
    res = []
    dfs(root, res)
    return res

dfs_postoder_recursive(x)

# check right subtree and then left subtree and reverse at the end
def dfs_postoder_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push left first, then right (so right gets processed first in reverse)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result[::-1]  # Reverse the result

dfs_postoder_iterative(x)