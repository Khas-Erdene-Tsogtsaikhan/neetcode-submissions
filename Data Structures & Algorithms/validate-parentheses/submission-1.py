class Solution:
    def isValid(self, s: str) -> bool:


        #use a stack, append to the list of stack first and then pop if corresponds
        #dictionary to store everything

        #"[()]]{}"
        #][(

        store = {
            "[":"]",
            "(":")",
            "{":"}",
            }

        stack = []
        for x in s:
            if x in store:
                stack.insert(0, x)
            else:
                if not stack:
                    return False
                if store[stack[0]] == x:
                    stack.pop(0)
                else:
                    return False
        return len(stack) == 0

        