import numpy as np

class Body:
    def __init__(self, mass: list, position: np.ndarray, velocity: np.ndarray, acceleration: np.ndarray):
        self.position = position
        self.mass = mass
        self.vel = velocity
        self.acc = acceleration

    def update(self, dt):
        self.vel = np.add(self.vel, np.multiply(self.acc, dt))
        self.position = np.add(self.position, np.multiply(self.vel, dt))
