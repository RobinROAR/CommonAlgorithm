#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########274. H-Index
#Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
#由研究者有 3 篇论文每篇至少被引用了 3 次
#Input: citations = [3,0,6,1,5]
#Output: 3
########思路
# 1. 排序     [0,1,3,5,6]
# 2. 遍历+逻辑


class Solution(object):
    def hIndex(self, nums):
        """
        :type citations: List[int]
        :rtype: int
        """
        #顺序排序
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        #[0,1,3,5,6]
        # 顺序遍历，nums[k]为引用数；大于这个引用的有n-k个(paper 数量)
        # 题目要求：researcher has 3 papers with at least 3 citations each and the remaining
        # two with no more than 3 citations each, her h-index is 3.
        # 举例： [2]  return 1 :  最多有1篇， 引用不小于1。
        for k in range(len(nums)):
            #用从左向右遍历保证最多，实际只会返回一次
            #返回的值是*数量*，不是引用
            #最多有h篇 <= h 引用
            # 没有则返回0

            if nums[k] >= len(nums) - k:
                return len(nums) - k

        return 0

sl = Solution()
#print sl.hIndex([3,0,6,1,5])
print sl.hIndex([1,2])