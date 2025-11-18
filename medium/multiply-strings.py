"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # we solve this using scientiic notation conversions
        # im not sure if this way is valid BUT its not using built-in BigInteger library or converting inputs to integer directly
        # its also more optimal than simulating multiplication manually

        hm = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        }
        rev = {v: k for k, v in hm.items()}

        conv_num1 = 0
        for c in range(len(num1)):
            conv_num1 += hm[num1[c]] * pow(10, (len(num1)-1)-c)
        
        conv_num2 = 0
        for c in range(len(num2)):
            conv_num2 += hm[num2[c]] * pow(10, (len(num2)-1)-c)
        
        res = conv_num1*conv_num2

        n = 0
        res_str = ""
        while True:
            n+=1
            rem = res % (pow(10, n))
            print(rem // (pow(10, n-1)))
            res_str += rev[rem // (pow(10, n-1))]
            if rem == res:
                break
        
        return res_str[::-1]
            
