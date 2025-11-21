class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        target = 0
        
        string1 = ''.join(str(d) for d in digits)
        
        len1 = len(string1)
        for i in range(len1):
            
            times = 10**(len1 - i - 1) 
            target += times * int(string1[i])
        target = target + 1
        string = str(target)
        len2 = len(string)
        res = []
        for i in range(len2):
            num = int(string[i])
            res.append(num)
        return res

  # shen ren methods. Only shen ren uses such method.
  
