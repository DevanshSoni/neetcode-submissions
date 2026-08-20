class Solution:
    def isValid(self, s: str) -> bool:
        opening_parenthetis = '('
        opening_dict = '{'
        opening_square_bracket = '['
        closing_parenthetis = ')'
        closing_dict = '}'
        closing_square_bracket = ']'
        closing_bracket_mapper = {
            closing_square_bracket: opening_square_bracket,
            closing_dict: opening_dict,
            closing_parenthetis: opening_parenthetis
        }

        stack = []
        for item in s:
            if not item in closing_bracket_mapper:
                stack.append(item)
            else:
                if stack and stack[-1] == closing_bracket_mapper[item]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False