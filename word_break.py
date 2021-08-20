
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict: return
        q = collections.deque()
        q.append(0)
        visited = [None]*len(s)
        while q:
            i = q.popleft()
            if not visited[i]:
                for j in range(i+1,len(s)+1):                 
                    if s[i:j] in wordDict:                    
                        if j == len(s):
                          return True  
                        q.append(j)
                visited[i]=True
