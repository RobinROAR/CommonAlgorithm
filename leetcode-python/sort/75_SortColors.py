#!/usr/bin/env python
# -*- coding: utf-8 -*-


###### 75 sort colors
#Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
###### 思路： 简单排序即可

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)-1):
            for j in xrange(i,len(nums)):
                if nums[i]>nums[j]:
                    nums[j],nums[i] = nums[i],nums[j]




