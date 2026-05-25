import math
import heapq
import itertools
import operator
from copy import deepcopy
from queue import PriorityQueue
from queue import Queue
from fractions import Fraction

# Helper functions
def read_int():
  return int(input())

def read_int_array():
  return list(map(int, input().split()))

def read_data():
  return input()

def read_data_array():
  return input().split()


# Problem script
test_cases = int(input())

for t in range(test_cases):

  # Example to parse a full line with data
  data = [int(x) for x in input().split()]

  print(f"{t + 1} {todo}")
