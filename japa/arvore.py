class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_branch(raiz, value):
    if raiz is None:
        return Node(value)
    else:
        if value < raiz.value:
            raiz.left = add_branch(raiz.left, value)
        else:
            raiz.right = add_branch(raiz.right, value)
    return raiz

def print_tree(raiz, space=0):
    if raiz is None:
        return
    
    space += 2

    print_tree(raiz.right, space)
    print(" " * space, raiz.value)
    print_tree(raiz.left, space)

def search_tree(raiz, value):
    if raiz is None:
        return
    if raiz.value == value:
        print("O valor existe na arvore")
        return raiz
    elif value > raiz.value:
        search_tree(raiz.right, value)
    elif value < raiz.value:
        search_tree(raiz.left, value)

raiz = None
raiz = add_branch(raiz,4)
raiz = add_branch(raiz,6)
raiz = add_branch(raiz,5)
raiz = add_branch(raiz,7)
raiz = add_branch(raiz,2)
raiz = add_branch(raiz,3)
raiz = add_branch(raiz,1)

# print_tree(raiz)

node = search_tree(raiz, 6)