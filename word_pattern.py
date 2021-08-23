lass Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ') # split s on space
        if len(s) != len(pattern): # compare lengths of split s with the pattern
            return False
        
        # 2 hashmaps. One contains the inverse of the other
        # ex: inward = { a : dog }, outward = { dog : a }
        inward = {}
        outward = {}
        
        # populate both maps by iterating over pattern and s
        # return False when faced with problems trying to fill both maps
        for i, j in zip(pattern, s):
            
            # check if i in inward, if not go ahead and add to inward map
            if not i in inward:
                # before adding i, make sure to check if j is already in outward
                # you dont want different inward keys to have the same value
                # if it already exists, return False, else, go ahead and add to outward map
                if not j in outward:
                    outward[j] = i
                else: return False
                
                inward[i] = j
            else:
                # if i is in inward, return False if j is not the same as the value stored in the inward map
                if j != inward[i]:
                    return False
