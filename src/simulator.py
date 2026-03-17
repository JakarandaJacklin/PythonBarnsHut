import quadtree as qt
import body as bd

import numpy as np

"""
This is the file that runs all the code for executing and repeating the simulation. Critically it has the function for summing 
forces
"""


theta_value = 1
g_value = 6.67e-11

def changeG(value):
    global g_value
    g_value = value

def changeTheta(value):
    global theta_value
    theta_value = value

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

def quadForceCalc(quad : qt.Quad, body : bd.Body):
    """
    The Big Boy function of the force calculation. This will traverse the tree and sum up forces if needed.
    """
    # Case one and halting condition: when we can use the Quad's COM approximation
    dist = findDist(quad.COM, body.position)
    # Also handle if the body is trying to find the COM of itself hehe
    if dist == 0:
        return [0, 0]

    if compareTheta(quad, body, dist) == True:
        lot = calcForce(quad.mass, body.mass, dist, quad.COM, body.position)
        if lot is None: # for debugging
            print("LOT IS NONE")
            return lot
        return lot
    
    # Case two, where we need to delve into the tree itself:
    else:
        forces = []
        for i in quad.Children:
            f = quadForceCalc(i, body)
            if f is None:
                print(f)
                print(i, body)
                print(i.COM, body.position)
                print(dist)
                print(calcForce(i.mass, body.mass, dist, i.COM, body.position))
                print(" END THIS TRAIN ")
        #print("hehe", forces)#
        #print(quad.Children)
        return(np.sum(forces, axis=0))
        #return forces
    #print("Poppycock")
    #print(compareTheta(quad, body, dist))
    
def bodyForceSum(quad, bodies):
    for i in bodies:
        force = quadForceCalc(quad, i)
        #print(force)

