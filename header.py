from collections import *
from typing import *
from heapq import *
from functools import *
from itertools import *
from math import *
from sortedcontainers import *
from bisect import *
from operator import *
from string import *
from random import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next