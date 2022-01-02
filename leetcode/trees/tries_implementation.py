class Node:
    def __init__(self, value, ):
        self.val = value
        self.isWord = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node(None)
        self.value_of_a = ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        for index, char in enumerate(word):
            if ord(char) - self.value_of_a not in curr.children:
                char_node = Node(char)
                curr.children[ord(char) - self.value_of_a]= char_node
                curr = char_node
            else:
                curr = curr.children[ord(char) - self.value_of_a]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if ord(char) - self.value_of_a in curr.children:
                curr = curr.children[ord(char) - self.value_of_a]
            else:
                return False
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if ord(char) - self.value_of_a in curr.children:
                curr = curr.children[ord(char) - self.value_of_a]
            else:
                return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
