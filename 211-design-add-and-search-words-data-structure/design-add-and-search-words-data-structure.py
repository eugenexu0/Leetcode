class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for s in word:
            if s not in current.children:
                current.children[s] = TrieNode()
            current = current.children[s]
        current.end = True

    def search(self, word: str) -> bool:
        ans = False
        def dfs(word, root: TrieNode, i: int):
            nonlocal ans
            #print(f'{word=}')
            #print(f'{i=}')
            if root.end and i == len(word):
                ans = True
            if i >= len(word) or not root:
                #print(f'{root=}')
                return
            if word[i] == ".":
                for _, child in root.children.items():
                    dfs(word, child, i+1)
            elif word[i] in root.children:
                #print(f'{word[i]=}')
                dfs(word, root.children[word[i]], i+1)
        dfs(word, self.root, 0)
        return ans

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)