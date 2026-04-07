import quadtree as qt
import body as bd

import numpy as np
import random
import time

"""
This is the file that runs all the code for executing and repeating the simulation. Critically it has the function for summing 
forces
"""

# Helper Functions

def findDist(quadPos, bodyPos):
    """
    Takes two position vectors and finds the distance between them.
    """
    return(np.sqrt(np.sum(np.square(np.subtract(quadPos, bodyPos)))))


def compareTheta(quad : qt.Quad, body : bd.Body, dist) -> bool:
    """
    Takes a quad and a body, and returns the distance size of the quad over the bodies' distance to 
    the center of mass. If it is less than theta we return true, if it is greater than or = theta we return false
    """
    theta = quad.size / dist # can prolly improve by not needing theta
    if theta < theta_value:
        return True
    else:
        return False
    
def calcForce(m1, m2, dist, p1, p2):
    """
    Calculates the gravitational force between two bodies.
    Returns the vector-ized form of force I guess
    """
    global g_value
    grav = g_value * m1 * m2
    vec = np.divide(np.subtract(p1, p2), dist**3)
    return (np.multiply(grav, vec))

def quadForceCalc(quad : qt.Quad, body : bd.Body, rem_list):
    """
    The Big Boy function of the force calculation. This will traverse the tree and sum up forces if needed.
    """
    # Case one and halting condition: when we can use the Quad's COM approximation
    dist = findDist(quad.COM, body.position)
    # Also handle if the body is trying to find the COM of itself or a body that has the same position as it
    if dist < np.sqrt(body.mass):#== 0:
        # First check to see if the body is the same object as this one
        if quad.cBody == None:
            #print("This is incredibly rare, but okay")
            pass
        elif body == quad.cBody:
            pass
        else:
            rem_list.append([body, quad.cBody])
        return [0, 0]


    if compareTheta(quad, body, dist) == True:
        lot = calcForce(quad.mass, body.mass, dist, quad.COM, body.position)
        return lot
    
    # Case two, where theta is greater than threshold:
    # Happens becuase either the quad is close and needs to be broken up further
    # Or happens when the quad has no children but still fails theta
    else:
        if quad.Children == []:
            lot = calcForce(quad.mass, body.mass, dist, quad.COM, body.position)
            return lot

        else:
            forces = []
            for i in quad.Children:
                f = quadForceCalc(i, body, rem_list)
                forces.append(f)
            
            l = np.sum(forces, axis=0)
            return(l)
        
    
def bodyForceSum(quad, bodies, dt=1):
    rem_list = []
    #te = time.time()
    for i in bodies:
        force = quadForceCalc(quad, i, rem_list)
        i.applyForce(force)
        i.update(quad_size, dt)
    #te = time.time() - te
    #print("it took", round(te * 1000), "ms to recalc the forces")
    removeExcessBodies(rem_list, bodies)
    


def slowForceCalc(bodies):
    for i in bodies:
        force = [0,0]
        for j in bodies:
            if i != j:
                dist = findDist(i.position, j.position)
                force += calcForce(i.mass, j.mass, dist, i.position, j.position)
        i.applyForce(force)
        i.update(500, 1)


def removeExcessBodies(rem_list, bodies):
    #print("removing", len(rem_list), "bodies from collisions")
    #te = time.time()
    for i in rem_list:
        if i[0].mass < i[1].mass:
            if i in bodies:
                bodies.remove(i[0])
                i[1].mass = i[1].mass + i[0].mass
        else:
            if i[1] in bodies:
                bodies.remove(i[1])
                i[0].mass = i[0].mass + i[1].mass
    #te = time.time() - te
    #print("it took", round(te * 1000), "ms to remove")



"""
Main Simulator interfacing Functions
"""

# Global Values

theta_value = 1
g_value = 6.67e-11

mass_range = [0,15]
position_range = [0,100]
quad_position = [0,0]
quad_size = 100

dist_scale = 1
# Functions to change global values

def changeG(value):
    global g_value
    g_value = value

def changeTheta(value):
    global theta_value
    theta_value = value

def changeQuads(pos, size):
    global quad_size
    global quad_position
    quad_size = size
    quad_position = pos

def changeBodis(mass_r, pos_r):
    global mass_range
    global position_range
    mass_range = mass_r
    position_range = pos_r




# Init Functions

def initBodies(num, min_mass, max_mass, min_pos, max_pos):
    """
    Returns a list of randomly generated bodies for simulating
    """
    bodies = []
    for i in range(num):
        bodies.append(bd.Body(random.randint(min_mass, max_mass), np.array([random.randint(min_pos, max_pos), random.randint(min_pos, max_pos)])))
    return bodies

def initTree(pos : list, size: float):
    """
    Initalizes the top quad of our tree
    """
    return(qt.Quad(np.array(pos), size))

# Main functions

def buildTree(quad, bodies, time=False):
    """
    Uses the list of bodies and the first level of the tree, inserts bodies and build the full quadtree
    Returns the quadtree. Can optionally report the time it took via console.
    """
    for i in bodies:
        qt.quadInsert(quad, i)
    return quad

def calcCOM(quad):
    """
    Calculates the COMs of the Quadtree
    """
    qt.quadCOM(quad)

def step(bodies, delta=False):
    """
    A function that does on full step of the Algorithm.
    Takes a list of bodies
    Uses the global Default Values
    """
    tree = initTree(quad_position, quad_size)
    tree = buildTree(tree, bodies)
    calcCOM(tree)
    bodyForceSum(tree, bodies)




