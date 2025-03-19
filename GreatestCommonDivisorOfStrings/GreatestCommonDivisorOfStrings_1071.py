class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        len1 = len(str1) #length of str1
        len2 = len(str2) #length of str2

        #greedily check if parameter divides str1 and str2
        def isDivisor(l):
            #check if length of substring is a factor of len1 and len2
            if len1 % l or len2 % l:
                return False
            #calculate the factors
            f1 = len1 // l
            f2 = len2 // l
            #check if multiplying factor to substrings equal full strings
            return str1[:l] *f1 == str1 and str1[:l] * f2 == str2



        
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:1]
        return "" #if no substring is found