class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()])
        L, R  = 0, len(s) - 1    
        
        while R > L:
            if s[L].lower() != s[R].lower():
                return False
            R -= 1
            L += 1

        return True