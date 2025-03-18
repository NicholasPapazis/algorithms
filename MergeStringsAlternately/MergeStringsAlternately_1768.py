class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i, j = 0, 0 #pointers to word1 and word2 respectively

        res = [] #array to hold the characers of the output.

        #check bounds of pointers
        while i < len(word1) and j < len(word2):
            res.append(word1[i])#append char from word1
            res.append(word2[i])#append char from word2
            i += 1 #increment pointer to word1
            j += 1 #increment pointer to word2
        res.append(word1[i:]) #add remaining characters of word1 to res (if there are any remaining)
        res.append(word2[j:]) #add remaining characters of word2 to res (if there are any remaining)

        return "".join(res) #convert res array to return string


#Test code
solution = Solution()
print("Case #1")
print(solution.mergeAlternately("abc", "pqr"))


print("Case #2")
print(solution.mergeAlternately("ab", "pqrs"))

print("Case #3")
print(solution.mergeAlternately("abcd", "pq"))
