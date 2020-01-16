

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



    def f(self,prices):
        minprice = float('inf')
        maxprofit = 0
        for i in range(len(prices)):

            if prices[i]<minprice:
                minprice = prices[i]
            elif prices[i] - minprice>maxprofit:

                maxprofit = prices[i]-minprice
        return maxprofit


#
S = Solution()
print(S.f([7,1,5,3,6,4]))

# Research environment functions
