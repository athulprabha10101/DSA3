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

    def min_value(self, current):
        while current.left is not None:
            current = current.left
        return current

    def max_value(self, current):
        while current.right is not None:
            current = current.right
        return current

    '''DELETE NODE :
    Traverse left or right so that left or right can be set to None, ie return None
    if node is None , ie value is not in the tree, return None
    if found: 4 possibilities:
        1 . is a leaf node > current node is set to None
        2.  has no left node, but has right node > current node is set to right node
        3.  has no left node, but has right node > current node is set to left node
        4.  has both right and left nodes, minvalue of right node is set as value of current node, min value left node None 
    '''
    def delete_node(self, value):
        self.delete_recur(self.root, value)

    def delete_recur(self, current, value):
        if current is None: # this part handles None edge case || x node - node to be deleted
            return None
        elif value < current.value: # searches for the node to be deleted recursively
            current.left = self.delete_recur(current.left, value) # this makes current.left = None, return from above
        elif value > current.value:
            current.right = self.delete_recur(current.right, value)
        else: # before this is for cases are for if the value is not in the tree, from here we look for the value
            if current.left is None and current.right is None: # is a leaf node
                return None # returns none to either of the 2 recursive calls above setting node to None or deleting it
            elif current.left is not None: # there are sub elements on the right after x node
                current = current.right # sends .left to earlier recursive call deleting the node and joining right to left
            elif current.right is not None:
                current = current.left
            else: # x node has subtrees on left and right
                sub_min = self.min_value(current.right) # finds min value in right subtree
                current.value = sub_min.value # sets min value as current node's value
                current.right = self.delete_recur(current.right, sub_min.value) # deletes the min node in right
        return True



# TESTS

bstr = Bs_tree()
bstr.insert(50)
bstr.insert(49)
bstr.insert(51)
bstr.insert(52)
bstr.insert(48)
bstr.insert(53)
bstr.insert(47)

print("Root ^ ", bstr.root.value)
print("Root.<- left ", bstr.root.left.value)
print("Root.right -> ", bstr.root.right.value)
print("Minimum value = ",(bstr.min_value(bstr.root)).value)
print("Maximum value = ", (bstr.max_value(bstr.root)).value)

