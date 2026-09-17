class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        graph = {")":"(" , "}" : "{", ']':'['}
        for char in s:
            if char in ")}]" and stack and graph[char] == stack[-1]:
                stack.pop()
            else :
                stack.append(char)
        return True if not stack else False
        