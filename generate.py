#-------------------------------------------------------------------------------
# Name:        РјРѕРґСѓР»СЊ1
# Purpose:
#
# Author:      the0
#
# Created:     21.06.2012
# Copyright:   (c) the0 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import *

def dfs(v):
    if v in b:
        return
    b.add(v)

    globals()["tin"][v] = t
    globals()["t"] += 1
    for x in globals()["children"][v]:
        dfs(x)
    globals()["tout"][v] = t
    globals()["t"] += 1

def is_parent(a, b, tin, tout   ):
    return globals()["tin"][a] <= globals()["tin"][b] and \
           globals()["tout"][a] >= globals()["tout"][b]

def main():
    seed()
    n = 10
    f = open("graph1.txt", "w")
    f.write(str(n) + "\n")

    globals()["children"] = [[] for _ in range(n)]
    globals()["t"] = 0
    globals()["b"] = set()
    globals()["tin"] = [0 for _ in range(n)]
    globals()["tout"] = [0 for _ in range(n)]
    for i in range(1, n):
        p = randrange(i)
        f.write("{0} {1} 1".format(p, i) + "\n")
        children[p].append(i)

    dfs(0)

    for i in range(n):
        for j in range(n):
            if not is_parent(i, j, tin, tout) and not is_parent(j, i, tin, tout) and random() < 0.5:
                f.write("{0} {1} 0".format(i, j) + "\n")

if __name__ == '__main__':
    globals()["t"] = 0
    globals()["tin"] = []
    globals()["tout"] = []
    globals()["children"] = []
    globals()["b"] = set()
    main()
