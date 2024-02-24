import numpy as np


class Lattice:
    def __init__(self, vec1, vec2, N, R, B):
        self.vec1 = vec1
        self.vec2 = vec2
        self.size = N
        self.spacing = R
        self.B = B

    def location(self, coord):
        return np.multiply(coord[0], self.vec1) + np.multiply(coord[1], self.vec2)

    def distance(self, coord1, coord2):
        return (
            np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
            ** self.spacing
        )

    def area(self, coord1, coord2, coord3):
        x1 = coord1[0]
        y1 = coord1[1]
        x2 = coord2[0]
        y2 = coord2[1]
        x3 = coord3[0]
        y3 = coord3[1]
        return (x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)) / 2
