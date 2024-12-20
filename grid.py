import heapq
import matplotlib.pyplot as plt
import numpy as np


class Grid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.grid = self._create_grid()

    def _create_grid(self):
        grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if (x, y) in self.obstacles:
                    row.append(1)  # Obstacle
                else:
                    row.append(0)  # Free space
            grid.append(row)
        return grid

    def is_valid(self, x, y):
        """Check if the position is within grid boundaries and not an obstacle."""
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles
