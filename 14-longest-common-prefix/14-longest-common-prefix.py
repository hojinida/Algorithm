class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        result=""
        for r in range(len(strs[0])):
            temp=""
            for c in range(len(strs)):
                temp+=strs[c][r]
            if len(temp)==temp.count(temp[0]):
                result+=temp[0]
            else:
                return result
        return result