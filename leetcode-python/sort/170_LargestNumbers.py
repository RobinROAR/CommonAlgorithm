#!/usr/bin/env python
# -*- coding: utf-8 -*-


###### 179. Largest Number
#Given a list of non negative integers, arrange them such that they form the largest number.
#Input: [10,2]
#Output: "210"
#
#Input: [3,30,34,5,9]
#Output: "9534330"
#Note: The result may be very large, so you need to return a string instead of an integer.
###### 思路：
# 1. 拆分问题， 拆分成两两拼合的问题， 找出最应该放在前面的数
# 2. 转化问题，通过修改排序准则，将问题转化为反向排序问题
# 3. 排序准则， 将单纯的大小比较，改成两个数拼接成的数字大小比较
# 4. 注意结果输出的特殊情况（0等）



class Solution(object):
    def largestNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i, -1, -1):
                if self.compare(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        # 输出结果：
        # 字符串拼接方法，需要首先转换list元素到str，要使用map函数，不要直接使用str(list)
        # 使用str(int)避免多余的0
        return str(int(''.join(map(str, nums))))

    def compare(self, num1, num2):
        return str(num1) + str(num2) > str(num2) + str(num1)



sl = Solution()

print sl.largestNumber([3,30,34,5,9])
