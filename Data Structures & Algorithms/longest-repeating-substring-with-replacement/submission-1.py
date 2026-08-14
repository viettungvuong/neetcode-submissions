class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        most_freq = 0

        l = 0
        r = 0

        n = len(s)
        res = 0

        while l<n and r<n:
            while r<n:
                if freq.get(s[r]) is None:
                    freq[s[r]]=0
                freq[s[r]]+=1
                
                most_freq_char, most_freq = max(freq.items(), key=lambda x: x[1])
                while l<n and (r-l+1)-most_freq>k:
                    freq[s[l]]-=1
                    l+=1
                    most_freq_char, most_freq = max(freq.items(), key=lambda x: x[1])
                res = max(res,r-l+1)
                r+=1
            
        
        return res

            
