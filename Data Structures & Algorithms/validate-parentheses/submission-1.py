class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_items = set("]})")
        for i in s:
            if i in close_items:
                if stack == []:
                    return False
                top = stack[-1]
                # Check if brackets dont match
                if (
                    (top == "(" and i != ")")
                    or (top == "[" and i != "]")
                    or (top == "{" and i != "}")
                ):
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
        