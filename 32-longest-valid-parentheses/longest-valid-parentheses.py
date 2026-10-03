class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0
        para = [-1]

        for i, j in enumerate(s):
            if j == '(':
                para.append(i)
            else:
                para.pop()
                if not para:
                    para.append(i)
                else:
                    count = max(count, i - para[-1])

        return count