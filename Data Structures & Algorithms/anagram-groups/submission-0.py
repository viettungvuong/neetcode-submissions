class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            anagram = "".join(sorted(s))
            if anagrams.get(anagram) is None:
                anagrams[anagram] = []
            anagrams[anagram].append(s)

        res = []
        for a in anagrams:
            res.append(anagrams[a])

        return res
