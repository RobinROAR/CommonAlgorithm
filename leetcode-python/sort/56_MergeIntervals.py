#!/usr/bin/env python
# -*- coding: utf-8 -*-

######### 56. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.
#Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
######## 思路：
# 先排序，第一位，第二位
# 两两比较, 合并时用删除
# 用while循环配合指针，因为有删除元素



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: (x.start, x.end))
        i = 0
        while i < len(intervals) - 1:
            if intervals[i].end > intervals[i + 1].end:
                intervals.remove(intervals[i + 1])
                #不要忽视这里 = 的情况
            elif intervals[i].end >= intervals[i + 1].start:
                intervals[i].end = intervals[i + 1].end
                intervals.remove(intervals[i + 1])
            else:
                i += 1
        return intervals

sl = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
sl.merge(intervals)
print intervals


