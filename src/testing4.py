import body
import quadtree
import random
import numpy as np
import sys
import time
import simulator

sys.setrecursionlimit(10000)
#print(sys.getrecursionlimit())

bodies = []
for i in range(10000):
    bodies.append(body.Body(random.randint(1, 15), np.array([random.randint(0, 100), random.randint(0, 100), ])))


te_time = time.time()

test = quadtree.Quad(np.array([0, 0]), 100)

for i in bodies:
    quadtree.quadInsert(test, i)

te_time = time.time() - te_time

print("it took", round(te_time * 1000), "ms to build the tree")

te_time = time.time()

quadtree.quadCOM(test)

te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to find the COM and prune the tree")

te_time = time.time()
simulator.bodyForceSum(test, bodies)
te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to do the forces")


te_time = time.time()

test = quadtree.Quad(np.array([0, 0]), 100)

for i in bodies:
    quadtree.quadInsert(test, i)

te_time = time.time() - te_time

print("it took", round(te_time * 1000), "ms to build the tree")

te_time = time.time()

quadtree.quadCOM(test)

te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to find the COM and prune the tree")

te_time = time.time()
simulator.bodyForceSum(test, bodies)
te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to do the forces")


te_time = time.time()

test = quadtree.Quad(np.array([0, 0]), 100)

for i in bodies:
    quadtree.quadInsert(test, i)

te_time = time.time() - te_time

print("it took", round(te_time * 1000), "ms to build the tree")

te_time = time.time()

quadtree.quadCOM(test)

te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to find the COM and prune the tree")

te_time = time.time()
simulator.bodyForceSum(test, bodies)
te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to do the forces")


te_time = time.time()

test = quadtree.Quad(np.array([0, 0]), 100)

for i in bodies:
    quadtree.quadInsert(test, i)

te_time = time.time() - te_time

print("it took", round(te_time * 1000), "ms to build the tree")

te_time = time.time()

quadtree.quadCOM(test)

te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to find the COM and prune the tree")

te_time = time.time()
simulator.bodyForceSum(test, bodies)
te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to do the forces")


te_time = time.time()

test = quadtree.Quad(np.array([0, 0]), 100)

for i in bodies:
    quadtree.quadInsert(test, i)

te_time = time.time() - te_time

print("it took", round(te_time * 1000), "ms to build the tree")

te_time = time.time()

quadtree.quadCOM(test)

te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to find the COM and prune the tree")

te_time = time.time()
simulator.bodyForceSum(test, bodies)
te_time = time.time()- te_time
print("it took", round(te_time * 1000), "ms to do the forces")
