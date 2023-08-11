# <u>Shortest Path Algorithm - Reverse Dijkstra's algorithm:</u>
### <u>Algorithm Overview</u>
The algorithm finds the shortest path between a source and a destination node in a graph.
It utilizes a cost matrix and a recursive approach.
>**The algorithm finds the shortest path using a reversed technique, where we backtrack the shortest paths from the destination node to the source node.**

### <u>Algorithm Steps:</u>
1. Initialize data structures for distances and paths.
2. Set destination node distance to 0 and path to the destination node itself.
3. Loop (V - 1) times (V is the number of nodes):
4. Find the unvisited node with the minimum distance.
5. Update distances and paths for neighboring nodes if shorter path is found.