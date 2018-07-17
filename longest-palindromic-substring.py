class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s: return ''

        space_list = [chr(0)] * len(s)
        s_with_space = [ch for t in zip(space_list, s) for ch in t] + [chr(0)]
        #print(s_with_space)
        s_with_space_len = len(s_with_space)

        max_half_length = 0
        max_middle = 0
        for middle in range(s_with_space_len):
            half_length = 0
            while middle - half_length >= 0 and middle + half_length < s_with_space_len \
                    and s_with_space[middle - half_length] == s_with_space[middle + half_length]:
                        half_length += 1
            if half_length > max_half_length:
                print (max_middle, max_half_length, half_length)
                max_half_length = half_length
                max_middle = middle
        max_half_length -= 1
        #print (max_middle, max_half_length)
        palindrome = s_with_space[max_middle - max_half_length : max_middle + max_half_length + 1]
        return ''.join([ch for ch in palindrome if ch != chr(0)])


s = Solution();
print(s.longestPalindrome(""))
print(s.longestPalindrome("b"))
print(s.longestPalindrome("bb"))
print(s.longestPalindrome("bbb"))
print(s.longestPalindrome("babbb"))
print(s.longestPalindrome("babbbb"))
print(s.longestPalindrome("babbbbi"))
print(s.longestPalindrome("babbbbii"))

print(s.longestPalindrome("bab"))
print(s.longestPalindrome("babb"))
print(s.longestPalindrome("babbab"))
print(s.longestPalindrome("babbabb"))
print(s.longestPalindrome("babbabbi"))
print(s.longestPalindrome("babbabbii"))

print('-' * 80)
print(s.longestPalindrome("babad"))
