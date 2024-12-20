from astar import a_star
class Agent:
    def __init__(self, id, start, goal):
        self.id = id
        self.start = start
        self.goal = goal
        self.path = []

    def plan_path(self, grid, reserved):
        self.path = a_star(grid, self.start, self.goal, reserved)
        return self.path
