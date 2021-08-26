class Solution(object):
    def longestPalindrome(self, s):
        def from_center(i,l,r):  # inspired by approach 4: take a char as the center and expand from it to check palidrome
            length_sub = 1 
            while  l >= 0 and r<= len(s) - 1 and s[l] == s[r]: # expand the palindrome
                length_sub = r - l + 1
                l = l - 1
                r = r + 1
            return length_sub
        
        longest = ""
        for i in range(0,len(s)):
            temp1 = from_center(i, i - 1, i + 1) # find the palindrome expanding from the char itself
            temp2 = from_center(i, i, i + 1) # find the palindrome expanding from the space after the char
            max_return = max(temp1, temp2) 
            if max_return > len(longest):
                if (max_return % 2 == 0):
                    longest = s[(i-(max_return/2) + 1): (i + max_return/2 + 1)] # python's [a:b] does not include the b element so have to add 1
                else:
                    longest = s[(i-(max_return/2)): (i + max_return/2 + 1)]
        return longest
