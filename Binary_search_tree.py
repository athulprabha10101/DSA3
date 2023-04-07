class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Bs_tree:
    def __init__(self):
        self.root = None

    def insert_iter(self, value):
        new_node = Node(value)
        if self.root is None:  # empty tree
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains_iter(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def contains(self, value):
        return self.contains_recur(self.root, value)

    def contains_recur(self, current, value):
        if current is None:
            return False
        elif value == current.value:
            return True
        elif value < current.value:
            return self.contains_recur(current.left, value)
        elif value > current.value:
            return self.contains_recur(current.right, value)

    def insert(self, value):
        if self.contains(value):
            return True
        else:
            new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_recur(self.root, new_node)

    def insert_recur(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self.insert_recur(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.insert_recur(current.right, new_node)

    def insert2(self, value):
        if self.root is None:
            self.root = Node(value)
        self.insert_recur2(self.root, value)

    def insert_recur2(self, current, value):
        if current is None:
            return Node(value)
        '''The function returns a new node to left or right given below when the when the recursion reaches None 
        recursively'''
        if value < current.value:
            current.left = self.insert_recur2(current.left, value)

        ''' the current node at the level is returned recursively till the root and is returned to the recur function which does not use it, the purpose is to pop the root call form the callstack '''
        if value > current.value:
            current.right = self.insert_recur2(current.right, value)
        return current
        ''' code is not required for when value == current.value as the code will return current node and the root call will be popped'''


bstr = Bs_tree()
bstr.insert(3)
bstr.insert(2)
print(bstr.root.left.value)
