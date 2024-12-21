from agent import Agent
from grid import Grid
from visualization import Visualizer
from simulation import Simulation
from astar import manhattan_heuristic, euclidean_heuristic

def main():
    width, height = 10, 10
    obstacles = [
        (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 4), (3, 4), (4, 4), (5, 4),
        (5, 3), (5, 2), (5, 1),
        (6, 1), (7, 1), (8, 1),
        (8, 2), (8, 3), (8, 4),
        (7, 4), (6, 4), (6, 5), (6, 6), (6, 7),
        (5, 7), (4, 7), (3, 7),
        (3, 6), (3, 5), (2, 5), (1, 5)
    ]

    grid = Grid(width, height, obstacles)

    num_agents = int(input("Enter the number of agents: "))
    agents = []

    for i in range(1, num_agents + 1):
        print(f"\nAgent {i}:")
        while True:
            try:
                start_x, start_y = map(int, input("Enter start position (x y): ").split())
                goal_x, goal_y = map(int, input("Enter goal position (x y): ").split())

                if not grid.is_valid(start_x, start_y):
                    print("Invalid start position. Please enter valid coordinates.")
                    continue
                if not grid.is_valid(goal_x, goal_y):
                    print("Invalid goal position. Please enter valid coordinates.")
                    continue

                agents.append(Agent(i, (start_x, start_y), (goal_x, goal_y)))
                break
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

    # Run simulation with Manhattan heuristic
    manhattan_simulation = Simulation(grid, agents)
    if manhattan_simulation.run(manhattan_heuristic):
        print("All agents have completed pathfinding with Manhattan heuristic.")
        for agent in agents:
            print(f"Agent {agent.id} path (Manhattan): {agent.path}")

        visualizer = Visualizer(grid, agents)
        print("Visualizing Manhattan heuristic paths...")
        visualizer.display(time_step=0.5)
    else:
        print("Pathfinding failed for one or more agents with Manhattan heuristic.")

    # For Euclidean heuristic, we need fresh agents (to avoid using already computed paths)
    agents_euclidean = [Agent(a.id, a.start, a.goal) for a in agents]
    euclidean_simulation = Simulation(grid, agents_euclidean)
    if euclidean_simulation.run(euclidean_heuristic):
        print("All agents have completed pathfinding with Euclidean heuristic.")
        for agent in agents_euclidean:
            print(f"Agent {agent.id} path (Euclidean): {agent.path}")

        visualizer_euclidean = Visualizer(grid, agents_euclidean)
        print("Visualizing Euclidean heuristic paths...")
        visualizer_euclidean.display(time_step=0.5)
    else:
        print("Pathfinding failed for one or more agents with Euclidean heuristic.")

if __name__ == "__main__":
    main()
