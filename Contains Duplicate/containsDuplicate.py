class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a set to store unique elements
        seen = set()
        
        # Iterate through the array
        for num in nums:
            # If the element is already in the set, return True
            if num in seen:
                return True
            # Otherwise, add it to the set
            seen.add(num)
        
        # If no duplicates were found, return False
        return False
