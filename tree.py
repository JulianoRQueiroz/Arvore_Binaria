

class Node:
    def __init__(self: object, data: None) -> None:
        self.data: None = data
        self.left: str = None
        self.right: str = None
        
    def __str__(self: object) -> str:
        return str(self.data)
        
class BinaryTree:
    def __init__(self: object, data=None) -> None:
        if data:
            node: str = Node(data)
            self.root = node
        else:
            self.root = None
    
    # percurso de ordem simetrica
    def simetric_traversal(self: object, node: None=None) -> Node:
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
          
if __name__ == "__main__":
    # tree = BinaryTree(7)
    # tree.root.left = Node(18)
    # tree.root.right = Node(14)
    
    # print(tree.root)
    # print(tree.root.right)
    # print(tree.root.left)
    tree: str = BinaryTree()
    n1: str = Node('a')
    n2: str = Node('+')
    n3: str = Node('*')
    n4: str = Node('b')
    n5: str = Node('-')
    n6: str = Node('/')
    n7: str = Node('c')
    n8: str = Node('d')
    n9: str = Node('e')
    
    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    
    tree.simetric_traversal()
    print()