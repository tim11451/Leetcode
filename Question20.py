class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        directionary = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in directionary: # i = ")/]/}", unfortunately, i spent innumerable hours to learn python but I still don't know how to indicate a value in directionary lol
                if len(stack) == 0:
                    return False
                if stack[-1] != directionary[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
