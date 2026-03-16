import numpy as np
import body
import quadtree

test = quadtree.Quad(np.array([0, 0]), 100)
quadtree.quadSplit(test)

test.report()
for i in test.Children:
    i.report()

print("now we create a body")

b = body.Body(12, np.array([0,51]))

test.cBody = b  # type: ignore
test.report()

print("Then we test the bump")
# then we test the bump
quadtree.quadBodyBump(test)

test.report()
for i in test.Children:
    i.report()

for i in range(5):
    print()

print("Now we test the quadBuild")
test = quadtree.Quad(np.array([0, 0]), 100)
b = body.Body(12, np.array([0,51]))
quadtree.quadInsert(test, b)
print("after one insert")
test.deepReport(0)

j = body.Body(12, np.array([10,10]))
quadtree.quadInsert(test, j)
print("after two inserts")
test.deepReport(0)

for i in range(5):
    print()

l = body.Body(12, np.array([15,15]))
quadtree.quadInsert(test, l)
print("after three inserts")
test.deepReport(0)




for i in range(10):
    print()

print(quadtree.sumCOM([[b.mass, b.position], [j.mass, j.position], [l.mass, l.position]]))


for i in range(10):
    print()
quadtree.quadCOM(test)
test.deepReport(0, True)
#print(test.Children)
