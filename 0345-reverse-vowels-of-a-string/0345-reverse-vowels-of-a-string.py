class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        Vowels = "aeiou"+"AEIOU"
        s_list = list(s)

        while left < right:
            if s_list[left] not in Vowels:
                left += 1
            if s_list[right] not in Vowels:
                right -= 1
            if s_list[right] in Vowels and s_list[left] in Vowels:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                right -= 1
                left += 1
            
        return ''.join(s_list)


        