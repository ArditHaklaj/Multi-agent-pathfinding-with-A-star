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

        for t in range(max_time):
            current_grid = grid_array.copy()
            plt.imshow(current_grid, cmap='Greys', origin='upper')

            for agent in self.agents:
                goal_x, goal_y = agent.goal
                plt.scatter(goal_x, goal_y, color='red', s=200, marker='s', edgecolor='black', label="Goal" if t == 0 else "")

            for i, agent in enumerate(self.agents):
                if t < len(agent.path):
                    x, y = agent.path[t]
                    agent_color = self.agent_colors[i % len(self.agent_colors)]
                    plt.scatter(x, y, color=agent_color, s=100, label=f'Agent {agent.id}' if t == 0 else "")

            plt.title(f"Time Step: {t}")
            plt.grid(visible=True, color='black', linestyle='-', linewidth=0.5)
            plt.xticks(np.arange(-0.5, self.grid.width, 1), [])
            plt.yticks(np.arange(-0.5, self.grid.height, 1), [])

            if t == 0:
                plt.legend(loc='upper left')

            plt.pause(time_step)
            plt.clf()

        # Final state
        plt.imshow(grid_array, cmap='Greys', origin='upper')
        for i, agent in enumerate(self.agents):
            x, y = agent.path[-1]
            plt.scatter(x, y, color=self.agent_colors[i % len(self.agent_colors)], s=100, label=f'Agent {agent.id} Final')

        plt.title("Final State")
        plt.grid(visible=True, color='black', linestyle='-', linewidth=0.5)
        plt.legend(loc='upper left')
        plt.show()
