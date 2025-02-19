# Using our array like a last-in-first-out stack, we loop throught the string, 
# adding open parens (those not belonging to the closers) to the array
# and removing them as we encounter the matching closing parens

class Solution:
    def isValid(self, s: str) -> bool:
        closers = {']':'[', '}':'{', ')':'('}
        arr = []

        for x in s:
            if x not in closers:
                arr.append(x)
            else:
                if len(arr) == 0:
                    return False
                if arr[-1] == closers[x]:
                    arr.pop()
                else:
                    return False

        return len(arr) == 0
