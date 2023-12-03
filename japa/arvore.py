class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# adiciona um novo nó na árvore
def add_branch(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = add_branch(root.left, value)
        else:
            root.right = add_branch(root.right, value)
    return root

# imprime a arvore
def print_tree(root, space=0):
    if root is None:
        return
    
    space += 2

    print_tree(root.right, space)
    print(" " * space, root.value)
    print_tree(root.left, space)

# procura um nó na arvore
def search_branch(root, value):
    if root is None or root.value == value:
        return root
    elif value > root.value:
        return search_branch(root.right, value)
    else:
        return search_branch(root.left, value)

# acha o menor valor daquela raiz
def find_minumum_value(root):
    if root is None or root.left is None:
        return root
    return find_minumum_value(root.left)

# acha o maior valor daquela raiz
def find_maximum_value(root):
    if root is None or root.right is None:
        return root
    return find_maximum_value(root.right)

# exclui um nó da arvore
def cut_branch(root, node_to_remove):
    if root is None:
        return root
    if node_to_remove.value < root.value:
        root.left = cut_branch(root.left, node_to_remove)
    elif node_to_remove.value > root.value:
        root.right = cut_branch(root.right, node_to_remove)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_maximum_value(root.left)
        root.value = temp.value
        root.left = cut_branch(root.left, search_branch(root.left, temp.value))
    return root

# verifica a largura da arvore
def verify_width_tree(root, size=0):
    return

def verif_height_tree(root, size):
    return

def postorder(root):
    if root is None:
        return root
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.value)

# verifica a profundidade da arvore

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

# node_to_remove = search_branch(root, 11)
# root = cut_branch(root, node_to_remove)

# print_tree(root)

# size = verify_width_tree(root)
postorder(root)