class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1 or n == 0:
            return 1
        
        nNeg = n < 0
        n = abs(n)
        
        i = 1
        origX = x
        
        while i < n:
            if (i*2) >= n:
                break
            x *= x
            i *= 2
            
        if abs(2*i - n) < abs(i-n):
            i *= 2
            x *= x
            while i > n:
                x /= origX
                i -= 1
        else:
            while i < n:
                x *= origX
                i += 1
    
        return 1/x if nNeg else x
