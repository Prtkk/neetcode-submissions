class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"(":")","{":"}","[":"]"}
        for b in s:
            if b in ["(","{","["]:
                stack.append(b)
            else:
                if not stack or match[stack[-1]]!=b:
                    return False
                stack.pop()
        
        return stack == []
        