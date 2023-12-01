#Pathfinding visualizer

![image](https://github.com/Rishabhv573/Pathfinding-Visualizer/assets/75075641/beaa2c20-208b-40f2-b0b4-416b6e68d6f1)

![image](https://github.com/Rishabhv573/Pathfinding-Visualizer/assets/75075641/bb08ceec-2948-4dbf-9932-53d824f0f0a6)


This Python program demonstrates pathfinding visualization using Pygame. The application allows users to create obstacles, set a starting point, and a target point. Two popular pathfinding algorithms, Dijkstra's Algorithm and A* Algorithm, can be chosen to find the shortest path between the start and target points.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [Controls](#controls)
- [Dependencies](#dependencies)

## Overview

The program creates a grid where users can interactively set barriers, a start node, and a target node. Users can choose between Dijkstra's Algorithm and A* Algorithm to find the shortest path from the start to the target.

## Features

- Interactive grid for creating obstacles and setting start/target nodes.
- Visualization of Dijkstra's Algorithm and A* Algorithm pathfinding.
- Clear the grid and start over with a single key press.
- Return to the main menu for algorithm selection.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/pathfinding-visualization.git
   cd pathfinding-visualization

## Uasge

- Click on the grid to create barriers, set the start node, and set the target node.
- Press the space bar to start the chosen algorithm for pathfinding.
- Press 'c' to clear the grid and start over.
- Press the backspace key to return to the main menu.

## Algorithms

The program supports two pathfinding algorithms:

1 Dijkstra's Algorithm:
- Guarantees the shortest path but may take longer to compute.
2 A Algorithm:*
- Uses heuristics to find the shortest path more efficiently than Dijkstra's Algorithm.

## Controls
- Left Mouse Click: Set barriers, start node, and target node.
- Right Mouse Click: Reset a node to its default state.
- Space Bar: Start the chosen pathfinding algorithm.
- 'c': Clear the grid and start over.
- Backspace Key: Return to the main menu.

## Dependencies
- Pygame
- queue
- heapq
