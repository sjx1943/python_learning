
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

    def f(self,root):
        levels = []
        if not root:
            return

        def help(node,level):
            if level == len(levels):
                levels.append([])

            if node.left:
                help(node.left,level+1)

            elif node.right:
                help(node.right,level+1)

        help(root,0)
        return levels

#
# S=Solution()
# print(S.f([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
#

