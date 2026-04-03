class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = maxLength = 0
        setOfSubstring = set()

        for right in range(len(s)):
            while s[right] in setOfSubstring:
                setOfSubstring.remove(s[left])
                left += 1

            setOfSubstring.add(s[right])

            maxLength = max(maxLength, right - left + 1)

        return maxLength
