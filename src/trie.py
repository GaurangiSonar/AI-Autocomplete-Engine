class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_word = True


    def search_prefix(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return None

            node = node.children[char]

        return node


    def collect_words(self, node, prefix, results):

        if node.is_word:
            results.append(prefix)

        for char in node.children:
            self.collect_words(
                node.children[char],
                prefix + char,
                results
            )