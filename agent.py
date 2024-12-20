from astar import a_star, manhattan_heuristic, euclidean_heuristic

class Agent:
    def __init__(self, id, start, goal):
        self.id = id
        self.start = start
        self.goal = goal
        self.path = []

    def plan_path(self, grid, reserved, heuristic_fn):
        self.path = a_star(grid, self.start, self.goal, reserved, heuristic_fn=heuristic_fn)
        return self.path
