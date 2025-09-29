class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dp(idx):
            # print(s, idx)
            if idx == len(s):
                return True
            found = False
            for word in wordDict:
                if s[idx:].startswith(word):
                    idx += len(word)
                    # temp = s[idx:] 
                    found |= dp(idx)
                    idx -= len(word)

            return found

        return dp(0)
                

