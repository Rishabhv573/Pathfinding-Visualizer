## It's a Pathfinding visualizer
# It uses A* Pathfinding algorithm and Dijkstra's algorithm as it's base to find the shortest path from begining to end
It uses python pygame to implement this algorithm

## A* 
It is a variant of Dijkstra's algorithm commonly used in games. A* assigns a weight to each open node equal to the weight of the edge to that node plus the approximate distance between that node and the finish. This approximate distance is found by the heuristic, and represents a minimum possible distance between that node and the end. This allows it to eliminate longer paths once an initial path is found. 

## Heuristics
A* uses this heuristic to improve on the behavior relative to Dijkstra's algorithm. When the heuristic evaluates to zero, A* is equivalent to Dijkstra's algorithm. As the heuristic estimate increases and gets closer to the true distance, A* continues to find optimal paths, but runs faster. When the value of the heuristic is exactly the true distance, A* examines the fewest nodes.

## Dijkstra's
Dijkstra's algorithm is used to find the shortest path from a given source node to all other nodes in a weighted graph. The algorithm works for graphs with non-negative edge weights. Here though we have considered equal weights for each edge. 
