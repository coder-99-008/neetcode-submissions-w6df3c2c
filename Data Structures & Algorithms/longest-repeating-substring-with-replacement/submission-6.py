class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        left = maxLength = maxFreq = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])

            while freq and (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength