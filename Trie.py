class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            current = current.children[letter]
        current.is_end = True

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_end

    def delete_word(self, word):
        self.recur_delete(self.root, word, 0)

    def recur_delete(self, current, word, index):
        if index == len(word):
            current.is_end = False
            return len(current.children) == 0

        char = word[index]
        if char not in current.children:
            return False

        delete_boolean = self.recur_delete(current.children[char], word, index+1)
        if delete_boolean:
            del current.children[char]
            return len(current.children) == 0

        return False


    def traverse(self):
        words = []

        def traverse_helper(node, word):
            if node.is_end:
                words.append(word)

            for char, child_node in node.children.items():
                traverse_helper(child_node, word + char)

        traverse_helper(self.root, '')
        return words


mytri = Trie()
mytri.insert("ABC")
mytri.insert("ABD")
mytri.insert("CBD")
print(mytri.root.children)
print(mytri.traverse())
