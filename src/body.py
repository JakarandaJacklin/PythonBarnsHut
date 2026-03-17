import numpy as np

class Body:
    def __init__(self, mass: float, position: np.ndarray, velocity: np.ndarray = np.array([0,0]), acceleration: np.ndarray = np.array([0,0])):
        self.position = position
        self.mass = mass
        self.vel = velocity
        self.acc = acceleration

    def update(self, dt):
        self.vel = np.add(self.vel, np.multiply(self.acc, dt))
        self.position = np.add(self.position, np.multiply(self.vel, dt))

    def applyForce(self, forceVec):
        self.acc = np.divide(forceVec, self.mass)
