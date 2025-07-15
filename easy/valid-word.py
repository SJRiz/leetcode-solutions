# A word is considered valid if:

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.

# Return true if word is valid, otherwise, return false.

class Solution:
    def isValid(self, word: str) -> bool:

        # If its less than 3 we already know its invalid
        if len(word) < 3:
            return False
        
        # We can lookup vowels in O(1) time, also state track the vowel and consonant
        vowels = {'a','e','i','o','u'}
        one_vowel = False
        one_consonant = False

        for char in word.lower():
            if not char.isalnum():
                return False
            if char in vowels:
                one_vowel = True

            # If the char is in the alphabet but not a vowel, we know its a consonant
            if char.isalpha() and char not in vowels:
                one_consonant = True
        
        return True if one_vowel and one_consonant else False
    
    # Solution is O(n) time and constant space