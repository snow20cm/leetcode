class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        max_len = 0
        strlen = len(s)
        charset = {s[0]}
        str_start = 0
        str_end = 1
        while str_start < strlen and str_end < strlen:
            #print(s[str_start], s[str_end])
            set_size = len(charset)
            charset.add(s[str_end])
            if set_size == len(charset) :
                max_len = max(max_len, set_size)
                while s[str_start] != s[str_end]:
                    charset.remove(s[str_start])
                    str_start += 1
                str_start += 1
            str_end += 1

        return max(max_len, len(charset))

s = Solution()

print(s.lengthOfLongestSubstring("ab"))
