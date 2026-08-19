class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if both string contain same characters with same frequency
        def count_char(string: str):
            char_count = {}
            for char in string:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

            return char_count

        if (len(s) != len(t)):
            return False

        char_count_in_s = count_char(s)
        char_count_in_t = count_char(t)

        for item in char_count_in_s:
            if item not in char_count_in_t or char_count_in_s[item] != char_count_in_t[item]:
                return False

        for item in char_count_in_t:
            if item not in char_count_in_s or char_count_in_t[item] != char_count_in_s[item]:
                return False

        return True
