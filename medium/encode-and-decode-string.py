# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

from typing import List
import math

class Solution:

    # Since this problem has a constraint of 0 <= length of strings <= 200, my approach to this problem was to put a 3-digit length infront of every substring.
    # Format: '003abc' for 'abc' (length 3). This ensures unambiguous decoding.
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            if len(string) != 0:

                # Find how many digits the length of the string contains
                x = 1 + math.floor(math.log(len(string), 10))

                # 1-x tells us how much zeroes we need to accomodate for the missing digits
                strlen = "0"*(3-x) + str(len(string))
            else:
                # Edge case if string = ""
                strlen = "000"
            
            # The final string will have the length of the substring + the substring itself
            result += strlen + string

        return result

    def decode(self, s: str) -> List[str]:

        # Handle edge case (which is if s = "000" or if the string was just "")
        if s == "000":
            return [""]

        result = []
        count = 0
        
        while count < len(s):
                # The first 3 digits tells the length of the string
                current_len = s[count:count+3]
                count += 3

                # We then turn the length table into an actual number
                length = int(current_len[0])*10**2 + int(current_len[1])*10 + int(current_len[2])

                # Once we have the length of the string, we iterate through its characters and make it a list, appending it to results
                current_str = s[count:count+length]
                result.append(current_str)

                # Next iteration will be past this length
                count += length

        return result
    
    # Time complexity for both encode and decode is O(n), where n is total number of characters. This approach is optimal, but slightly less robust and clean
    # I should have used a delimiter approach, and I was not aware of the builtin zfill function
    # Nonetheless, I figured this solution out myself and its optimal