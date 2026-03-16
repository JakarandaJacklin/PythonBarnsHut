import body
import numpy as np

"""
This file has all the functions and code for step one of the Barnes Hut Tree Algorithm.
That means it contains all the code for BUILDING the Quad Tree.
"""

class Quad:
    """
    Quad classes are the bounding boxes of a quadtree that containes the size and the position.
    They also contain all the bodies of the quadrant for later processing, as well as mass and COM
    and children references. The building boxes of Quadtree.
    """
    def __init__(self, pos, size):
      # Set up the basic information about the quad
      self.pos = pos #As a np.array
      self.size = size
      self.COM = np.array([0, 0]) #COM stands for Center of Mass, will use the global posion
      self.mass = 0
      self.numBody = 0
      
      # Set up the pointers towards the "children" of the Quad
      self.cBody = body.Body # For the body it has (only if a leaf node)
      self.Children = [] # For the other quads it might have. Wait I can probably make this one thing but hey

    def report(self, mass=False):
        if mass == False:
           print("this quad has position of", self.pos, "and size of", self.size, "with body count", self.numBody, "and body of", self.cBody)
        else:
           print("this quad has mass of", self.mass, "and COM of", self.COM)

    def deepReport(self, level, mass = False):
       self.report(mass)
       if len(self.Children) > 0:
           print("and for my children at level", level)
           for i in self.Children:
               i.deepReport(level + 1, mass)


def quadSplit(quad: Quad):
    """
    We are going to assume that we already know a quad has NO children here.
    """
    newSize = quad.size / 2
    quad.Children = [Quad(quad.pos, newSize), Quad(np.add(quad.pos, [newSize, 0]), newSize), Quad(np.add(quad.pos, [0, newSize]), newSize), Quad(np.add(quad.pos, newSize), newSize)]


def whichQuad(quad: Quad, position):
    """
    Take a position, and a Quad object, and tells which children of the quad object the position
    would be in.
    Does NOT assume that the Quad object has quad children
    DOES assume that the position falls within the Quad
    """
    if position[0] > (quad.pos[0] + (quad.size / 2)):
        if position[1] > (quad.pos[1] + (quad.size / 2)):
            return 3
        else:
            return 1
    else:
        if position[1] > (quad.pos[1] + (quad.size / 2)):
            return 2
        else:
            return 0
        

def quadBodyBump(quad):
    """
    Takes the body already assigned to a quad and bumps it down a level to the children.
    DOES assume that the Quad already has children
    DOES assume that those children are empty quads though
    """
    b = quad.cBody
    quad.cBody = None #del quad.cBody
    quad.Children[whichQuad(quad, b.position)].cBody = b
    quad.Children[whichQuad(quad, b.position)].numBody = 1




def quadInsert(quad: Quad, body: body.Body):
    """
    Builds the quadtree, and inserts into it if needed. The Big boy functiuon (tm)
    """
    # Step One - See if the Quad we are in has no children, handle.
    if quad.numBody == 0:
        quad.cBody = body # type: ignore
        quad.numBody = 1
        # Then we can stop
    
    # Step Two - handle the cases where the quad is NOT empty - For one body
    elif quad.numBody == 1:
        quadSplit(quad)
        quadBodyBump(quad)
        quad.numBody += 1
        quadInsert(quad.Children[whichQuad(quad, body.position)], body)

    # Step Three - handle the case where the quad is NOT empty AND it has already been split
    else:
        quad.numBody += 1
        quadInsert(quad.Children[whichQuad(quad, body.position)], body)


def sumCOM(coms):
    mass = 0
    com = np.array([0,0])
    for i in coms:
        mass = mass + i[0]
        com = np.add(np.multiply(i[1], i[0]), com)
    com = np.divide(com, mass)
    return [mass, com]


# Now we do the Center of Mass handling. This function will also prune the treem removing quads with no bodies.
def quadCOM(quad: Quad):
    """
    DOES assume that it will never get passed an empty quad
    """
    if quad.numBody == 1:
        quad.mass = quad.cBody.mass # type: ignore
        quad.COM = quad.cBody.position # type: ignore
        return [quad.mass, quad.COM]
    else:
        coms = []
        pops = []
        for i in quad.Children:
            if i.numBody == 0:
                pops.append(i)
            else:
                coms.append(quadCOM(i))
        for i in pops:
            #i.report()
            quad.Children.remove(i)
        com = sumCOM(coms)
        quad.mass = com[0]
        quad.COM = com[1]
        return [quad.mass, quad.COM]