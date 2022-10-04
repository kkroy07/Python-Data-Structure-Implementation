class BinarySerachTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            #add data into left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySerachTree(data)
        else:
            #add data into right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySerachTree(data)

def inorder_tr(root):
    if root:

        inorder_tr(root.left)
        print(root.data)
        inorder_tr(root.right)

def build_tree(elements):
    root = BinarySerachTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__ == "__main__":
    nums = [42,51,12,34,10,56,23]
    root = build_tree(nums)
    inorder_tr(root)