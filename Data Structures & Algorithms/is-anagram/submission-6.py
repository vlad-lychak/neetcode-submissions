class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(s)):
            countS[ord(s[i]) - ord('a')] += 1
            countT[ord(t[i]) - ord('a')] += 1

        return countS == countT



        

