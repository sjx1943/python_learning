

from matplotlib.font_manager import FontProperties
# font_set = FontProperties(fname = r"/Library/Fonts/Microsoft/SimSun.ttf",size=15)
import random
import pylab
import numpy as np
import pandas as pd
import re
import heapq
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swap(self,nums,i,j):
        tmp=nums[i]
        nums[i]=nums[j]
        nums[j]=tmp

    def reverse(self,nums,start):
        i=start
        j=len(nums)-1
        while i<j:
            self.swap(nums,i,j)
            i+=1
            j-=1
        return nums



    def f(self,numRows):
        traingle= []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0]=1
            row[-1]=1

            for j in range(1,len(row)-1):
                row[j] = traingle[row_num-1][j-1]+traingle[row_num-1][j]

            traingle.append(row)

        return traingle
#
S = Solution()
print(S.f(5))

# Research environment functions
