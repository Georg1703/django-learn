class Solution(object):
    def bitwiseComlememt(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev_binar = []
        binary_representation = bin(n)[2:]
        for i in binary_representation:
            if i == "0":
                rev_binar.append("1")
            else:
                rev_binar.append("0")
        
        binary_string = ''.join(rev_binar)
        back_to_zecimal = int(binary_string, 2)
        print(back_to_zecimal)

s = Solution()
s.bitwiseComlememt(300)
'''
I learned the bin() method 
that transforms numbers into 
their binary form
'''