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
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal, reserved):
    open_list = []
    heapq.heappush(open_list, (0, start, 0, []))  # (f, (x, y), g, path)
    visited = set()

    while open_list:
        f, current, g, path = heapq.heappop(open_list)
        if (current, g) in visited:
            continue
        visited.add((current, g))

        path = path + [current]
        if current == goal:
            return path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current[0] + dx, current[1] + dy
            next_time = g + 1

            if grid.is_valid(next_x, next_y):
                # Check for vertex conflicts
                if (next_x, next_y) in reserved.get(next_time, []):
                    continue
                # Check for edge conflicts
                if (current, (next_x, next_y)) in reserved.get(next_time, []):
                    continue
                heapq.heappush(open_list, (
                    g + 1 + heuristic((next_x, next_y), goal),
                    (next_x, next_y),
                    next_time,
                    path
                ))
    return None
