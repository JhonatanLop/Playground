class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_branch(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = add_branch(root.left, value)
        else:
            root.right = add_branch(root.right, value)
    return root

def print_tree(root, space=0):
    if root is None:
        return
    
    space += 2

    print_tree(root.right, space)
    print(" " * space, root.value)
    print_tree(root.left, space)

def search_branch(root, value):
    if root is None or root.value == value:
        return root
    elif value > root.value:
        return search_branch(root.right, value)
    elif value < root.value:
        return search_branch(root.left, value)

def find_minumum_value(root):
    if root is None or root.left is None:
        return root
    return find_minumum_value(root.left)

def find_maximum_value(root):
    if root is None or root.right is None:
        return root
    return find_maximum_value(root.right)

def cut_branch(root, value):
    node = search_branch(root, value)
    if node is None:
        return root

# def cut_branch(root, value):
#     if root is None:
#         return root
#     if value < root.value:
#         root.left = cut_branch(root.left, value)
#     elif value > root.value:
#         root.right = cut_branch(root.right, value)
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         temp = find_maximum_value(root.left)
#         root.value = temp.value
#         root.left = cut_branch(root.left, temp.value)
#     return root

root = None
root = add_branch(root,4)
root = add_branch(root,6)
root = add_branch(root,5)
root = add_branch(root,2)
root = add_branch(root,3)
root = add_branch(root,1)
root = add_branch(root,0)
root = add_branch(root,11)
root = add_branch(root,-2)
root = add_branch(root,10)
root = add_branch(root,-1)
root = add_branch(root,9)
root = add_branch(root,7)
root = add_branch(root,8)
root = add_branch(root,12)
root = add_branch(root,13)

# print_tree(root)

# node = search_branch(root, 6)
# print(node)

# minimum_value = find_minumum_value(root)
# max_value = find_maximum_value(root)
# print(minimum_value)
# print(max_value)

# print(find_maximum_value(root.left))

root = cut_branch(root, 4)
print_tree(root)
