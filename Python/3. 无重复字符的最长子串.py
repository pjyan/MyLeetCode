#https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#遇到重复时，找到最近重复的踢掉，保留新的字符串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        tmp_str = ''
        tmp_len = 0
        for i in s:
            if i not in tmp_str:
                tmp_str +=i
                tmp_len +=1
            else:        #重复了
                length = max(length, tmp_len)   #记录当前长度
                tmp_str = tmp_str[tmp_str.rfind(i)+1:] + i   #找到重复字符串位置，踢掉生成新数组
                tmp_len = len(tmp_str)   #计算新数组长度
                
        return  max(length, tmp_len) #可能一个重复的都没有再比较一把