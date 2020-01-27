

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
        k_max=2
        n = len(prices)
        if n==0:
            return 0
        dp = [[[0,0],[0,0],[0,0]] for _ in range(n)]
        # dp = [[[0, 0, 0], [0,0,0]] for _ in range(n)]
        # dp[-1][k_max][1] = -float('inf')
        # dp[-1][k_max][0] = 0
        for i in range(n):
            for k in range(k_max,0,-1):
                if i-1==-1:
                    dp[i][k][0]=0
                    dp[i][k][1]=-prices[0]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])


            # dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            # dp[i][1] = max(dp[i - 1][1], dp[i-1][0]-prices[i])

        return dp[n-1][k_max][0]


S = Solution()
print(S.f([3,3,5,0,0,3,1,4]))

# Research environment functions

