# Multi-agent-pathfinding-with-A-star

## Description
This project simulates a multi-agent pathfinding problem, where several agents navigate through a grid with obstacles to reach their respective goals. The simulation ensures that paths avoid collisions using a modified A* algorithm that considers agent paths at each time step.

### Features
1. **Cooperative A***: Implements a cooperative A* algorithm to avoid collisions between agents.
2. **Visualization**: Provides a visual representation of agents' movements, including delays and detours.
3. **Flexible Input**: Accepts user-defined grid dimensions, obstacles, and start/goal points for agents.

## Requirements
- Python 3.8+
- `matplotlib`
- `numpy`

Install dependencies with:
```bash
pip install matplotlib numpy
```

## Files
- **agent.py**: Defines the `Agent` class, responsible for path planning using the A* algorithm.
- **astar.py**: Contains the grid definition and the A* algorithm implementation.
- **grid.py**: Handles grid creation and obstacle validation.
- **main.py**: Entry point of the application.
- **simulation.py**: Simulates the agents' paths, ensuring no conflicts.
- **visualization.py**: Visualizes the agents' movements through the grid.

## Usage
1. Run the `main.py` script:
   ```bash
   python main.py
   ```
2. Enter the number of agents.
3. Specify the start and goal positions for each agent.
4. Observe the simulation and visualization of agents' movements.

## Input Format
- **Grid**: Defined with obstacles specified as a list of `(x, y)` coordinates.
- **Agents**: Each agent has a start and goal position provided during runtime.

## Output
- Conflict-free paths for all agents.
- Visualization of agents' movements.

## Example
```text
Enter the number of agents: 2

Agent 1:
Enter start position (x y): 0 0
Enter goal position (x y): 9 9

Agent 2:
Enter start position (x y): 9 0
Enter goal position (x y): 0 9
```

## Algorithm Details
### Modified A*
- **Heuristic**: Uses Manhattan distance.
- **Reservation Table**: Tracks reserved positions at each time step to avoid conflicts.
- **Edge Conflicts**: Ensures agents do not swap positions at the same time.

## Visualization
- Displays the grid with obstacles and agents' movements.
- Agents are represented by distinct colors, and their goals are marked in red.
- Animates step-by-step movements with adjustable time intervals.

## Students
-Ardit Haklaj
-Elda Drenica
-Erite Hyseni
