class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        #idea is construct a graph connecting two words that differ
        #by 1 letter 
        hashmap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i+1:]
                hashmap[temp].append(word)
        for i in range(len(beginWord)):
            temp = beginWord[:i] + "*" + beginWord[i+1:]
            hashmap[temp].append(beginWord)
        #print(f'{hashmap=}')
        adjList = defaultdict(list)
        for key, val in hashmap.items():
            if len(val) >= 2:
                for i in range(len(val)):
                    for j in range(i + 1, len(val)):
                        adjList[val[i]].append(val[j])
                        adjList[val[j]].append(val[i])
        #print(adjList)
        queue = deque([beginWord])
        ans = 1
        visited = set()
        while queue:
            templen = len(queue)
            for i in range(templen):
                node = queue.popleft()
                visited.add(node)
                if node == endWord:
                    return ans
                if node not in adjList:
                    continue
                for neighbor in adjList[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            ans += 1
        return 0
