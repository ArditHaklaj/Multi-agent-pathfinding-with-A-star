from agent import Agent
from grid import Grid
from visualization import Visualizer
from simulation import Simulation


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

                # Validate positions
                if not grid.is_valid(start_x, start_y):
                    print("Invalid start position. Please enter valid coordinates.")
                    continue
                if not grid.is_valid(goal_x, goal_y):
                    print("Invalid goal position. Please enter valid coordinates.")
                    continue

                agents.append(Agent(i, (start_x, start_y), (goal_x, goal_y)))
                break
            except ValueError:
                print("Invalid input format. Please enter two integers separated by a space.")

    simulation = Simulation(grid, agents)

    if simulation.run():
        print("All agents have completed pathfinding.")
        for agent in agents:
            print(f"Agent {agent.id} path: {agent.path}")

        # Visualize the paths
        visualizer = Visualizer(grid, agents)
        visualizer.display(time_step=0.5)  # Adjust time_step for animation speed
    else:
        print("Pathfinding failed for one or more agents.")


if __name__ == "__main__":
    main()
