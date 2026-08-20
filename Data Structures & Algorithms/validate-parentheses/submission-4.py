class Solution:
    def isValid(self, s: str) -> bool:
        opening_parenthetis = '('
        opening_dict = '{'
        opening_square_bracket = '['
        closing_parenthetis = ')'
        closing_dict = '}'
        closing_square_bracket = ']'
        opening_brackets = [opening_square_bracket, opening_dict, opening_parenthetis]
        closing_brackets = [closing_parenthetis, closing_dict, closing_square_bracket]
        closing_bracket_mapper = {
            closing_square_bracket: opening_square_bracket,
            closing_dict: opening_dict,
            closing_parenthetis: opening_parenthetis
        }

        stack = []
        for item in s:
            if item in opening_brackets:
                stack.append(item)
            elif item in closing_brackets:
                if len(stack) == 0:
                    return False

                respective_opening_bracket = closing_bracket_mapper[item]
                current_stack_last_item = stack.pop()
                if not current_stack_last_item == respective_opening_bracket:
                    return False

        return True if not stack else False