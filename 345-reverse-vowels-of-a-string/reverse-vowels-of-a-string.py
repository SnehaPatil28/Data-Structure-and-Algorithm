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


    # def reverseVowels(s: str) -> str:
    # vowels = set("aeiouAEIOU")
    # s_list = list(s)
    # left, right = 0, len(s_list) - 1
    
    # while left < right:
    #     while left < right and s_list[left] not in vowels:
    #         left += 1
    #     while left < right and s_list[right] not in vowels:
    #         right -= 1
        
    #     # Swap vowels
    #     s_list[left], s_list[right] = s_list[right], s_list[left]
    #     left += 1
    #     right -= 1
        
    # return "".join(s_list)

            
            
