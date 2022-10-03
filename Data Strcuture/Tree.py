class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        space = ' ' * self.get_level()*3
        prefix = space + "|--" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level


def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cell = TreeNode("Cell Phone")
    cell.add_child(TreeNode("Iphone"))
    cell.add_child(TreeNode("Google pixel"))
    cell.add_child(TreeNode("Realme"))

    tv= TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("MI"))
    tv.add_child(TreeNode("Apple"))

    root.add_child(laptop)
    root.add_child(cell)
    root.add_child(tv)
    return root


if __name__ == '__main__':
    root = build_product_tree()
   # print(root.get_level())
    root.print_tree()

"""
Expected OutPut
Electronics
   |--Laptop
      |--Mac
      |--Surface
      |--Thinkpad
   |--Cell Phone
      |--Iphone
      |--Google pixel
      |--Realme
   |--TV
      |--Samsung
      |--MI
      |--Apple




"""


