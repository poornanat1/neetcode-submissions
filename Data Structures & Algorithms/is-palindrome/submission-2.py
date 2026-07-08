class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(s.split()).lower()
        i = 0
        j = len(s_clean)-1
        while i<=j:
            if s_clean[i].isalnum()==False:
                i+=1
            if s_clean[j].isalnum()==False:
                j-=1
            if i>j:
                return True
            if s_clean[i]!=s_clean[j]:
                return False
            i+=1
            j-=1
        return True
        

        
        