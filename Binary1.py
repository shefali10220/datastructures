class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        print("printing current self",self.data)
        if data == self.data:
            return # node already exist

        if data < self.data:
            print("left node data",self.data)
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            print("right node data", self.data)
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        print("printing elements",elements)
        if self.left:
            elements += self.left.in_order_traversal()
            print("in elements left ,",elements)
            print(self.left.data)

        elements.append(self.data)
        print("node ",elements)
        if self.right:
            elements += self.right.in_order_traversal()
            print("in elements right ,",elements)
            print(self.right.data)


        return elements


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())