class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        output = 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1 
        
            charSet.add(s[right])
            output = max(output, right - left + 1)
        
        return output
