

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

    def reverse(self,head):
        cur=head
        prev=None
        while cur:
            nxt=cur.next
            cur.next = prev
            prev = cur
            cur=nxt
        return prev

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # dummy = defaultdict(lambda:None(0))
        # dummy[None]=None
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None
        right = self.reverse(right)
        pt = dummy
        while left or right:
            if left:
                dummy.next = left
                left=left.next
                dummy = dummy.next
            if right:
                dummy.next = right
                right = right.next
                dummy = dummy.next


S = Solution()
print(S.f([[2],[3,4],[6,5,7],[4,1,8,3]]))

# Research environment functions
