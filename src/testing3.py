import simulator
import time
import sys
import visual


print(simulator.findDist([51, 12], [4, 17]))
print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)

bodies = simulator.initBodies(250, 1, 15, 0, 100)
#print(bodies)

steps = 1000000

tel = 0

screen = visual.init(100)

for i in range(steps):
    #print(len(bodies))
    te = time.time()
    simulator.step(bodies)
    te = time.time() - te
    print("it took", round(te * 1000), "ms to do one step")
    tel = tel + te
print("For the entire simulator of", steps, "steps, it took", round(tel, 3), "s to do the entire thing")


def vis():
    visual.screen_init(screen)
    for i in bodies:
        visual.draw(screen, i.position, i.mass)
    visual.screen_update

