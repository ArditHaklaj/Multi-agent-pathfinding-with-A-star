import heapq
import math

def manhattan_heuristic(a, b):
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean_heuristic(a, b):
    """Euclidean distance heuristic."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def a_star(grid, start, goal, reserved, heuristic_fn=manhattan_heuristic):
    # Each state in the priority queue: (f, (x, y), g, path)
    # f = g + heuristic; g = time step
    open_list = []
    heapq.heappush(open_list, (0, start, 0, []))
    visited = set()

    # Allowed moves: up, right, down, left, and wait in place
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]

    while open_list:
        f, current, g, path = heapq.heappop(open_list)

        # Check if this state is already visited with the same time
        if (current, g) in visited:
            continue
        visited.add((current, g))

        new_path = path + [current]

        if current == goal:
            return new_path

        for dx, dy in directions:
            next_x = current[0] + dx
            next_y = current[1] + dy
            next_time = g + 1

            # Check validity of the next cell (or waiting in place)
            if (dx == 0 and dy == 0) or grid.is_valid(next_x, next_y):
                # Check vertex conflict
                if (next_x, next_y) in reserved.get(next_time, []):
                    continue

                # Check edge conflict (no swapping positions)
                if g in reserved and (next_x, next_y) in reserved[g]:
                    # Another agent was here at time g.
                    # If at next_time that agent moves into our current, it would be a swap.
                    if (next_time in reserved) and (current in reserved[next_time]):
                        continue

                new_f = next_time + heuristic_fn((next_x, next_y), goal)
                heapq.heappush(open_list, (new_f, (next_x, next_y), next_time, new_path))

    return None
