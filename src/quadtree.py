import body
import numpy as np

class Quad:
    """
    Quad classes are the bounding boxes of a quadtree that containes the size and the position.
    They also contain all the bodies of the quadrant for later processing
    """
    def __init__(self, center: float, size: float) -> None:
        self.center = center
        self.size = size



class Node:
    """
    Node classses wraps up all the complex stuff of quads and relates it to the tree in a simple and easy
    way to follow. Or something. 
    """
    def __init__(self) -> None:
        self.children = []
         


def quadInsert(node: Node, body: body.Body) -> None:
    pass