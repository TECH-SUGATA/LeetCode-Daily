class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        ans = []
        
        for w in words:
            s = set(w.lower())
            if any(s <= r for r in rows):
                ans.append(w)
                
        return ans