

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self) -> str:
        return str(self.data)
        
class BinaryTree:
    def __init__(self, data) -> None:
        node = Node(data)
        self.root = node
        
if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(18)