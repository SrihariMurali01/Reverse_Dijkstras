import sys
import numpy as np


class Dj:

    def __init__(self, cost_matrix):
        self.cost_matrix = np.array(cost_matrix)

    def find_shortest_path(self, source, destination):

        num_nodes = self.cost_matrix.shape[0]

        # Check if source and destination nodes are within valid range
        if source < 0 or source >= num_nodes or destination < 0 or destination >= num_nodes:
            return [None, None]  # Return a special value to indicate invalid input

        shortest_distance = np.full(num_nodes, sys.maxsize, dtype=np.int64)
        shortest_path = np.empty((num_nodes,), dtype=object)
        visited = np.full(num_nodes, False)

        shortest_distance[source] = 0
        shortest_path[source] = [source]

        for _ in range(num_nodes):
            min_distance = sys.maxsize
            current_node = None

            # Find the unvisited node with the shortest distance
            for node in range(num_nodes):
                if not visited[node] and shortest_distance[node] < min_distance:
                    min_distance = shortest_distance[node]
                    current_node = node

            if current_node is None:
                break

            visited[current_node] = True

            # Update distances and paths for neighboring nodes
            for neighbor in range(num_nodes):
                if not visited[neighbor] and self.cost_matrix[current_node][neighbor] > 0:
                    new_distance = shortest_distance[current_node] + self.cost_matrix[current_node][neighbor]
                    if new_distance < shortest_distance[neighbor]:
                        shortest_distance[neighbor] = new_distance
                        shortest_path[neighbor] = shortest_path[current_node] + [neighbor]

        if shortest_path[destination] is None and shortest_distance[destination] == sys.maxsize:
            return [None, None]

        return [shortest_path[destination], shortest_distance[destination]]
