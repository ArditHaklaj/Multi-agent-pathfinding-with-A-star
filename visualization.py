import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self, grid, agents):
        self.grid = grid
        self.agents = agents
        self.agent_colors = ['blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink', 'gray']

    def display(self, time_step=1):
        grid_array = np.array(self.grid.grid)
        max_time = max(len(agent.path) for agent in self.agents)

        # Set up the figure so each cell appears as a 1x1 square.
        # Increase the figure size as needed for clarity.
        plt.figure(figsize=(self.grid.width, self.grid.height), dpi=80)

        for t in range(max_time):
            plt.clf()  # Clear the figure for each time step
            # Display the grid as a 2D image with each cell clearly defined
            plt.imshow(grid_array, cmap='Greys', origin='upper',
                       interpolation='none', aspect='equal')

            # Set the ticks to align with cell boundaries
            plt.xticks(np.arange(-0.5, self.grid.width, 1), [])
            plt.yticks(np.arange(-0.5, self.grid.height, 1), [])
            plt.grid(visible=True, color='black', linestyle='-', linewidth=0.5)

            # Plot the goals
            for agent in self.agents:
                goal_x, goal_y = agent.goal
                plt.scatter(goal_x, goal_y, color='red', s=200, marker='s', edgecolor='black', 
                            label="Goal" if t == 0 else "")

            # Plot agent positions
            for i, agent in enumerate(self.agents):
                if t < len(agent.path):
                    x, y = agent.path[t]
                    agent_color = self.agent_colors[i % len(self.agent_colors)]
                    plt.scatter(x, y, color=agent_color, s=100, label=f'Agent {agent.id}' if t == 0 else "")

            plt.title(f"Time Step: {t}")
            if t == 0:
                plt.legend(loc='upper left')

            plt.pause(time_step)

        # Final state with trails
        plt.clf()
        plt.imshow(grid_array, cmap='Greys', origin='upper',
                   interpolation='none', aspect='equal')

        plt.xticks(np.arange(-0.5, self.grid.width, 1), [])
        plt.yticks(np.arange(-0.5, self.grid.height, 1), [])
        plt.grid(visible=True, color='black', linestyle='-', linewidth=0.5)

        # Plot final positions and trails
        for i, agent in enumerate(self.agents):
            agent_color = self.agent_colors[i % len(self.agent_colors)]
            # Final position
            final_x, final_y = agent.path[-1]
            plt.scatter(final_x, final_y, color=agent_color, s=100, label=f'Agent {agent.id} Final')

            # Trail of the path
            path_x = [pos[0] for pos in agent.path]
            path_y = [pos[1] for pos in agent.path]
            plt.plot(path_x, path_y, color=agent_color, linewidth=2, linestyle='--')

        plt.title("Final State with Trails")
        plt.legend(loc='upper left')
        plt.show()
