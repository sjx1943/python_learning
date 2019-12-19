

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



    def f(self,s):

        n=len(s)
        if n==0:
            return 0
        dp=[0]*n
        res=0
        for i in range(n):
            if i>0 and s[i]==")":

                if s[i-1]=="(":
                    dp[i]=dp[i-2]+2
                elif s[i-1]==")" and i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1]=="(":
                    dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]

                if dp[i]>res:
                    res=dp[i]

        return res
#
# S = Solution()
# print(S.f([1,2,3]))

# Research environment functions
