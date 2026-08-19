class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.strip().lower().replace(" ", "")
        processed_string = ""
        for item in string:
            if item.isalnum():
                processed_string = processed_string+item

        reversed_string = processed_string[::-1]
        for index in range(0, len(processed_string)):
            if processed_string[index] != reversed_string[index]:
                return False

        return True

        # if processed_string == reversed_string:
        #     return True
        # else:
        #     return False
