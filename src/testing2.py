import body
import quadtree
import random
import numpy as np
import sys

sys.setrecursionlimit(1000000)
print(sys.getrecursionlimit())

bodies = []
for i in range(1000):
    bodies.append(body.Body(random.randint(1, 15), np.array([random.randint(0, 100), random.randint(0, 100), ])))

test = quadtree.Quad(np.array([0, 0]), 100)

for i in bodies:
    quadtree.quadInsert(test, i)

quadtree.quadCOM(test)

test.deepReport(0, True)