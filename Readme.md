# <u>Shortest Path Algorithm - Based on Reverse tracking from destination, using Dynamic Programming:</u>
### <u>Algorithm Overview</u>
The algorithm finds the shortest path between a source and a destination node in a graph.
It utilizes a cost matrix and an iterative approach.
>**The algorithm finds the shortest path using a reversed technique, where we backtrack the shortest paths from the destination node to the source node.
>It can also be modified at the return statement to find the shortest paths in the "destination" perspective. The algortihm can also be considered as a mix of Floyd's and Dijkstra's Shortest Parth Finding algorithms.**

> The algorithm works for unidirectional, bidirectional, multistage, and negative weighted graphs. 
### <u>Algorithm :</u>
#### Input:
- <u>cost_matrix</u>: 2D matrix representing edge costs between nodes
- <u>source</u>: Starting node
- <u>destination</u>: Ending node

#### Output:
- <u>shortest_path</u>: List containing the shortest path from source to other nodes


#### Procedure:
1. Initialize num_nodes as the number of nodes in cost_matrix.
2. Initialize visited as a boolean array of size num_nodes, all elements set to False.
3. Initialize shortest_distance as an array of size num_nodes, all elements set to a very large value.
4. Initialize shortest_path as an array of empty lists, size num_nodes.
5. Set **shortest_distance[destination]** to 0 and **shortest_path[destination]** to **[destination]**.
6. Repeat for i from 1 to **num_nodes - 1**
   1. Initialize **min_distance** as a very large value (sys.maxsize) and current_node as None.
   2. For each node in 0 to num_nodes - 1:
      - **If node is unvisited (not visited[node]) and shortest_distance[node] < min_distance:**
         - Update min_distance with shortest_distance[node].
         - Set current_node as node.
   3. If current_node is None, break the loop.
   4. **Mark current_node as visited (visited[current_node] = True).**
   5. For each prev_node in 0 to num_nodes - 1:
      - If there's a positive edge from prev_node to current_node (cost_matrix[prev_node][current_node] > 0):
      -  _Remove this part to work with negative graphs only_
         - Calculate new_distance as shortest_distance[current_node] + cost_matrix[prev_node][current_node].
         - **If new_distance < shortest_distance[prev_node]**:
            - *Update shortest_distance[prev_node] with new_distance.*
            - *Update shortest_path[prev_node] by copying shortest_path[current_node] and appending prev_node.*
7. Return shortest_path[source] and shortest_distance[source] as the shortest path from source to other nodes along with the cost of the shortest 
   path as a "list".

#### _Add this code in "Runner" class to see the output of the algorithm:_

```python
a = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]]

ob = Runner(a)
res = ob.find_shortest_path(0, 4)
print(res)
```
#### _The Cost matrix for the above given data, for reference purposes._
<img src="https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg">

#### For negative-weighted graphs (make sure to edit the code)

```python
a = [[0, -1, 0, 3],
     [0, 0, -2, 0],
     [0, 0, 0, 0],
     [0, 0, 4, 0]]
ob = Runner(a)
print(ob.find_shortest_path(0,2))
```