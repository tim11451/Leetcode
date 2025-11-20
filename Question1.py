class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution = [-1,-1]
        len1 = len(nums)
        for i in range(len1):
            for j in range(i+1,len1):
                if (nums[i]+nums[j]==target):
                    return [i,j]
        return solution                

# Loser's solution. Pure brute force, just letting me memorize the experience that being slapped by primary school teacher.
# Unfortunate, weak
# also nov, very cold that day
