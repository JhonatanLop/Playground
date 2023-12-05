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

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.value)

    # encontra um nó e retorna o mesmo
    def find_branch(self, value):
        if self is None or self.value == value:
            return self
        elif value < self.value:
            return self.left.find_branch(value)
        else:
            return self.right.find_branch(value)

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
    
    #TODO
    # pensar em uma forma de fazer o balanceamento da arvore
    # pensar em passar o nó a ser removido no parâmetro
    # verifica a altura da arvore:
    # apaga um nó da arvore
    def cut_branch(self, value=None):
        node_to_remove = self.find_branch(value)
        if node_to_remove is None:
            return self
        if self.value < node_to_remove.value:
            self.right = self.right.cut_branch(value)
        elif self.value > node_to_remove.value:
            self.left = self.left.cut_branch(value)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            temp_value = self.left.find_max_value().value
            self.value = temp_value
            self.left = self.left.cut_branch(temp_value)
        return self

    def find_height(self, node=None):
        h_left = 0
        h_right = 0
        if self.left:
            h_left = self.left.find_height(self.left)
        if self.right:
            h_right = self.right.find_height(self.right)
        if h_right > h_left:
            return h_right + 1
        return h_left + 1

if __name__ == "__main__":
    tree = Node(4)
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
    # maximum = tree.find_max_value()
    # print(maximum.value)
    # print(maximum.value)
    # tree.cut_branch(-2)
    tree.print_tree()
    # tree.print_postorder()
    # print(tree.find_height())