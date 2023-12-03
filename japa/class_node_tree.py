class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return(self.value)

    # adiciona um novo nó
    def add_branch(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add_branch(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add_branch(value)
        return self
    
    # printa a arvore
    def print_tree(self, space=0):
        if self.right:
            self.right.print_tree(space + 2)
        print(" " * space, str(self.value))
        if self.left:
            self.left.print_tree(space + 2)

    # encontra um nó e retorna o mesmo
    def find_branch(self, value):
        if self is None or self.value == value:
            return self
        elif value < self.value:
            if self.left is not None:
                return self.left.find_branch(value)
        else:
            if self.right is not None:
                return self.right.find_branch(value)
        return None
    
    # encontra o menor nó de uma arvore
    def find_minimum_value(self):
        if self is None:
            return self
        elif self.left is not None:
            return self.left.find_minimum_value()
        return self
    
    # encontra o maior nó de uma estrutura de arvore
    def find_max_value(self):
        if self is None:
            return self
        elif self.right is not None:
            return self.right.find_max_value()
        return self


if __name__ == "__main__":
    tree = Node(4)
    tree.add_branch(4)
    tree.add_branch(6)
    tree.add_branch(5)
    tree.add_branch(2)
    tree.add_branch(3)
    tree.add_branch(1)
    tree.add_branch(0)
    tree.add_branch(11)
    tree.add_branch(-2)
    tree.add_branch(10)
    tree.add_branch(-1)
    tree.add_branch(9)
    tree.add_branch(7)
    tree.add_branch(8)
    tree.add_branch(12)
    tree.add_branch(13)
    # tree.print_tree()

    # root = tree.find_branch(6)
    # print(root)
    # minimum = tree.find_minimum_value()
    # print(minimum.value)
    maximum = tree.find_max_value()
    print(maximum.value)