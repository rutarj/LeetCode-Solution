class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if lengths are equal
        if len(s) != len(t):
            return False
        
        # Create dictionaries to store character counts for both strings
        char_count_s = {}
        char_count_t = {}
        
        # Populate char_count_s dictionary with character counts from string s
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        
        # Populate char_count_t dictionary with character counts from string t
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        # Compare character counts in both dictionaries
        return char_count_s == char_count_t