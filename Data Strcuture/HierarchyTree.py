'''
Below is the Implementation of the exercise given by codebasic on github link below
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
'''


class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level

    def print_tree(self, val):
        if val == "both":
            space = ' ' * self.get_level() * 3
            prefix = space + "|--" if self.parent else ""

            print(prefix + self.name, "(", self.designation, ")")
            for child in self.children:
                child.print_tree("both")
        elif val == "name":
            space = ' ' * self.get_level() * 3
            prefix = space + "|--" if self.parent else ""

            print(prefix + self.name)
            for child in self.children:
                child.print_tree("name")
        elif val == "designation":
            space = ' ' * self.get_level() * 3
            prefix = space + "|--" if self.parent else ""

            print(prefix + self.designation)
            for child in self.children:
                child.print_tree("designation")




def build_tree():
    root = TreeNode("Nilupul", "CEO")
    cto = TreeNode("Chinmay","CTO")
    infral = TreeNode("Vishwa", "Infrastructure Lead")
    cm = TreeNode("Dhaval", "Cloud Manager")
    am = TreeNode("Abhijit", "App Manager")
    ah = TreeNode("Aamir", "Application Head")
    cto1 = TreeNode("Gels", "HR Head")
    rm = TreeNode("Peter", "Recruitment Manager")
    rm1 = TreeNode("Waqas", "Policy Manager")


    root.add_child(cto)
    root.add_child(cto1)
    cto.add_child(infral)
    cto1.add_child(rm)
    cto1.add_child(rm1)
    cto.add_child(ah)
    infral.add_child(cm)
    infral.add_child(am)

    return root


if __name__ == '__main__':
    root = build_tree()
   # print(root.get_level())
    root.print_tree("both")
'''
root.print_tree("designation")
CEO
   |--CTO
      |--Infrastructure Lead
         |--Cloud Manager
         |--App Manager
      |--Application Head
   |--HR Head
      |--Recruitment Manager
      |--Policy Manager
**********************************************
root.print_tree("name")
Nilupul
   |--Chinmay
      |--Vishwa
         |--Dhaval
         |--Abhijit
      |--Aamir
   |--Gels
      |--Peter
      |--Waqas

**********************************
root.print_tree("both")
Nilupul ( CEO )
   |--Chinmay ( CTO )
      |--Vishwa ( Infrastructure Lead )
         |--Dhaval ( Cloud Manager )
         |--Abhijit ( App Manager )
      |--Aamir ( Application Head )
   |--Gels ( HR Head )
      |--Peter ( Recruitment Manager )
      |--Waqas ( Policy Manager )
      
  

'''