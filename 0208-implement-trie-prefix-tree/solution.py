class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        # time  : O(n), n is the lenght of str
        # space : O(n)
        
        cur = self.root
        
        for char in word:
            if char not in cur: cur[char] = {}            
            cur = cur[char]
            
        cur['#'] = True
        

    def search(self, word: str) -> bool:
        # time  : O(n)
        # space : O(1)
        
        cur = self.root
        
        for char in word:
            if char not in cur: return False
            cur = cur[char]
            
        return '#' in cur
        

    def startsWith(self, prefix: str) -> bool:
        # time  : O(n)
        # space : O(1)
        
        cur = self.root
        
        for char in prefix:
            if char not in cur: return False
            cur = cur[char]
            
        return True
