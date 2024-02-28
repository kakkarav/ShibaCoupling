import numpy as np


class Lattice:
    def __init__(self, vec1: np.ndarray, vec2: np.ndarray, R: float) -> None:
        self.vec1 = np.array(vec1)
        self.vec2 = np.array(vec2)
        self.spacing = R

    def location(self, coord: np.ndarray) -> np.ndarray[float, float]:
        """
        Calculate the absolute coordinate in distance
        """
        return (coord[0] * self.vec1 + coord[1] * self.vec2) * self.spacing

    def distance(self, coord1: np.ndarray, coord2: np.ndarray) -> float:
        """
        Calculate the distance between two points
        """
        return np.linalg.norm(self.location(coord1) - self.location(coord2))

    def phase(self, B: float, coord1: np.ndarray, coord2: np.ndarray) -> float:
        """
        Calcualte the Aharonov-Bohm phase betwen two points
        A = B(-y,x)/2
        """
        x1, y1 = self.location(coord1)
        x2, y2 = self.location(coord2)
        normalization = 1
        return normalization * B * (x1 * y2 - x2 * y1) / 2

    def area(self, coord1, coord2, coord3):
        """
        Calcuate the area of a triangle formed by three points
        The sign of the area depends on the order of three points using the right hand rule
        """
        x1, y1 = self.location(coord1)
        x2, y2 = self.location(coord2)
        x3, y3 = self.location(coord3)
        return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
