class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        n1_count = [0] * 26
        n2_count = [0] * 26

        if n1 > n2:
            return False

        for i in range(n1):
            n2_count[ord(s2[i]) - 97] += 1
            n1_count[ord(s1[i]) - 97] += 1           
        
        if n1_count == n2_count:
            return True

        for i in range(n1, n2):
            n2_count[ord(s2[i]) - 97] += 1     
            n2_count[ord(s2[i - n1]) - 97] -= 1
            if n1_count == n2_count:
                return True   
    
        return False