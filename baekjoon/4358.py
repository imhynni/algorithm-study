# https://www.acmicpc.net/problem/4358
# 백준 4358 <생태학>
# Silver 2
from collections import defaultdict
import sys


def solution():
    trees = defaultdict(int)
    total = 0
    for line in sys.stdin:
        tree = line.rstrip()
        trees[tree] += 1
        total += 1
    trees = sorted(trees.items())
    for k, v in trees:
        rate = (v / total) * 100
        print('%s %.4f' % (k, rate))


solution()
