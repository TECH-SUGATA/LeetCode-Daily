class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        first = len(s) % k
        ans = s[:first]
        
        for i in range(first, len(s), k):
            if ans:
                ans += "-"
            ans += s[i:i+k]
        
        return ans