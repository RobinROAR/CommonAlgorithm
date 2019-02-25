#!/usr/bin/env python
# -*- coding: utf-8 -*-

######### 524.
#Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string.
#If there are more than one possible results, return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
#Input: s = "abpcplea", d = ["ale","apple","monkey","plea"]
# Output: apple"
######## 思路：
# 1. 根据要求先对d进行排序：长度，字典顺序
# 2. 进行匹配： 将s逐位置与d比较， 以d中单词的长度为界
class Solution(object):
    def findLongestWord(self, s, d):
        #对d进行排序，长度，字典顺序
        d.sort(key=lambda x: (-len(x),x) )
        # 比较逻辑
        for word in d:
            #对于每个单词进行判断，设置指针；判断指针的位置，以及i是否等于word【k】
            k = 0
            for i in s:
                if k<len(word) and i == word[k]:
                    k+=1
            if k == len(word):
                return word
        return ""

s = "abpcplea"
d = ["ale","apple","monkey","plea"]

sl = Solution()

print sl.findLongestWord(s,d)


