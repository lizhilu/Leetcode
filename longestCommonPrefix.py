class Solution:
    def common_Prefix(self, a, b):
        lenA = len(a)
        lenB = len(b)
        index = 0
        res = 0
        while (index < lenA and index <lenB):
            if (a[index] != b[index]):
                break;
            res = res +1
            index = index + 1
    
        return res
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ""
        if (len(strs) == 1):
            return strs[0]
        index = 0;
        longest = -1
        while(index < len(strs) - 1):
            tmp = self.common_Prefix(strs[index],strs[index+1])
            if (tmp == 0):
                return ""
            if (longest < 0 or tmp < longest):
                longest = tmp
            index = index + 1
        return strs[0][0:longest]
