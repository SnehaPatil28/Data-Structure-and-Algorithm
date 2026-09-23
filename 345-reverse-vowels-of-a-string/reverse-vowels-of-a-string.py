class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        char = list(s)
        vowel = []
        for i in range(n):
            if s[i] in "aeiouAEIOU":
                vowel.append(i)

        m = len(vowel)
        for i in range(m//2):
            char[vowel[i]], char[vowel[m-i-1]] = char[vowel[m-i-1]] , char[vowel[i]]
        
        return "".join(char)
            
            
