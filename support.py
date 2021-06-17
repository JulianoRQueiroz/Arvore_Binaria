from tree import BinaryTree, Node

if __name__ == '__main__':
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