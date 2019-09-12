
from collections import Counter
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname = r"/Library/Fonts/Microsoft/SimSun.ttf",size=15)
import random
import pylab
import pandas as pd
import re
import collections
import heapq
import glob
import math
from numpy import dot
import numpy as np
from numpy.linalg import inv
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from collections import defaultdict
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def hasPathSum(self,root,sum):
        if not root:
            return False
        sum-=root.val

        if not root.left and not root.right:
            return sum==0

        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)








#
S=Solution()
a=S.f([3,9,20,15,7],[9,3,15,20,7])


# print(a.val)
#

# print('hell')