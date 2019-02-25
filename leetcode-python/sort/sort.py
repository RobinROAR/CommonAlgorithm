#!/usr/bin/env python
# -*- coding: utf-8 -*-

### 实现各种排序方法
## 快速排序，归并排序
## 冒泡排序，插入排序，选择排序
### Robin


import random

#################  快速排序
### 递归，将序列分为大于key和小于key的两个序列，然后递归
## 时间复杂度不稳定。平均 nlogn（需要划分logn次，每次比较n次）。最坏 n^2(每次都在开头或者末尾，划分n次，比较n次）
def quick_sort(nums):
    #key为一个数，两个指针 low, high
    key = nums[0]
    low = 0
    high = len(nums)-1
    # 循环结束时low=high=key的位置
    while low<high:
        # 第一步，high指针左移。
        while (low<high and nums[high]>key):
            high-=1
        #碰到第一个 < key的值，交换 low,high的值 。
        # 此时key的值转移到high的位置，所以下个循环时直接交换low、high即可
        # 当low=high时，交换无意义
        nums[high],nums[low] = nums[low],nums[high]

        # 第二布，low指针右移
        while low < high and nums[low]< key:
            low+=1
        #找到第一个low>key的值，交换low,high
        nums[low],nums[high] = nums[high],nums[low]

    # 递归过程，根据key的位置，具体分三种情况
    #key不在开头，排序之前部分
    if (low > 0):
        #使用递归时，需要对元数组重新赋值。否则会产生变量名不匹配
        nums[:low] = quick_sort(nums[:low])
        #key在中间，再排序后面的部分
        if (low < len(nums) - 1):
            nums[low + 1:] = quick_sort(nums[low + 1:])
    # 如果key在开头，排序后面的部分
    elif (low == 0 and len(nums) > 1):
        nums[low + 1:] = quick_sort(nums[low + 1:])
    else:
        return nums
    return nums

#print quick_sort([6,8,5,7,4])

################# 归并排序
### 递归，对序列不断二分，然后将排序好的子序列不断的合并。
## 时间复杂度稳定。 nlogn  需要logn次划分，每次比较n次（新建一个数组一个个放), 需要额外O（n）个空间。
def merge_sort(nums):
    if len(nums)>1:
        #二分
        mid = len(nums)/2
        #该操作新建变量,不共享
        left = nums[:mid]
        right = nums [mid:]
        merge_sort(left)
        merge_sort(right)

        #归并,将左右序列的数比较，按次序放入新的nums中
        l,r = 0,0
        k = 0

        #三个归并逻辑
        #当左右都有剩余
        while l<len(left) and r<len(right):
            if left[l] < right[r]:
                nums[k] = left[l]
                k+=1
                l+=1
            else:
                nums[k] = right[r]
                k+=1
                r+=1
        #当right已经没有元素
        while l<len(left):
            nums[k] = left[l]
            k+=1
            l+=1
        #当left已经没有元素
        while r<len(right):
            nums[k] = right[r]
            k+=1
            r+=1

#################  冒泡排序
# 稳定 O(n^2)
def bubble_sort(nums):
    # 两层循环嵌套。
    # 每一个元素冒泡 0 -- n-1  冒泡 = 找一个最小的，放在第一个位置
    # 每一次冒泡时与后面元素比较  i -- n
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                # 可以用如下方式直接交换元素
                nums[i], nums[j] = nums[j], nums[i]

    return nums

############ 选择排序
# 每一趟从待排序的的序列中选出最小的，把最小的放在首位；
# 时间： O(n2) 递归n次，比较n次  稳定     空间 O（1）
def selection_sort(nums):
    #分比较子集时，最后一个不用比;循环n次(n,后n-1,后n-2...)
    for i in range(len(nums)-1):
        #设第一个为最小
        min_idx = i
        #后面的跟第一个比，记录最小的坐标
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_idx]:
                min_idx = j
        #吧最小的放在最前面
        if min_idx!=i:
            nums[i],nums[min_idx] = nums[min_idx],nums[i]
    return nums

############# 插入排序
# 每次向头部序列插入一个数，然后排序头部序列
# 时间： O(n2) 递归n次，比较n次；  稳定；     空间 O（1）
def insertion_sort(nums):
    #相当于每次往头部插入一个数，第一个不用比u
    for i in range(1,len(nums)):
        #倒叙比较序列内，从最后一个，到第一个
        for j in range(i,0,-1):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]


    return nums





def test(testfunction):
    #结果
    list = [range(1), range(10), range(100), range(1001)]
    #测试数据
    slist = [range(1), range(10), range(100), range(1001)]
    for i in slist:
        random.shuffle(i)

    # 排序前
    for j in range(len(list)):
        print list[j] == slist[j],
        testfunction(slist[j])

    print '\n'
    # 排序后
    for j in range(len(list)):
        print list[j] == slist[j],



def bub(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums



test(bub)



