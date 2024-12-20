class Simulation:
    def __init__(self, grid, agents):
        """
        Initializes the simulation with the grid and agents.
        
        :param grid: The grid object representing the environment.
        :param agents: List of agents participating in the simulation.
        """
        self.grid = grid
        self.agents = agents
        self.reservation_table = {}

    def validate_paths(self, heuristic_fn):
        """
        Validates and plans conflict-free paths for all agents using cooperative A*.
        
        :return: True if all agents have valid paths, False otherwise.
        """
        for agent in self.agents:
            print(f"Planning path for Agent {agent.id} with {heuristic_fn.__name__}...")
            path = agent.plan_path(self.grid, self.reservation_table, heuristic_fn)
            if not path:
                print(f"Agent {agent.id} could not find a conflict-free path!")
                return False

            # Reserve the path for this agent
            for t, pos in enumerate(path):
                if t not in self.reservation_table:
                    self.reservation_table[t] = []
                self.reservation_table[t].append(pos)

            print(f"Agent {agent.id} path: {path}")
        return True

    def run(self, heuristic_fn):
        """
        Executes the simulation by validating and running the agents' paths 
        for the given heuristic function.

        :return: True if the simulation completes successfully, False otherwise.
        """
        print(f"Starting simulation with {heuristic_fn.__name__}...")
        if not self.validate_paths(heuristic_fn):
            print("One or more agents failed to find a path.")
            return False

        print("All agents have conflict-free paths.")
        return True
