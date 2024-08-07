class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        element_count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[element_count] = nums[i]
                element_count += 1
        return element_count
    
    
print(Solution().removeElement([3, 2, 2, 3], 3))