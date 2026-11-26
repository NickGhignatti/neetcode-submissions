class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        chars = {}
        for char in s:
            if chars.get(char):
                chars[char] += 1
            else:
                chars[char] = 1
        for char in t:
            if not chars.get(char) or chars[char] == 0:
                return False
            chars[char] -= 1
        
        return True