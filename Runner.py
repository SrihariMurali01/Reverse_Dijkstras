import sys
import numpy as np


class Runner:

    def __init__(self, cost_matrix):
        self.cost_matrix = np.array(cost_matrix)

    def find_shortest_path(self, source, destination):

        # Check if source and destination nodes are within valid range
        if source < 0 or source >= self.cost_matrix.shape[0] or destination < 0 or destination >= self.cost_matrix.shape[0]:
            return [None, None]  # Return a special value to indicate invalid input

        num_nodes = self.cost_matrix.shape[0]
        visited = np.full(num_nodes, False)
        shortest_distance = np.full(num_nodes, sys.maxsize, dtype=np.int64)
        shortest_path = np.empty((num_nodes,), dtype=object)

        shortest_distance[destination] = 0
        shortest_path[destination] = [destination]

        for _ in range(num_nodes - 1):
            min_distance = sys.maxsize
            current_node = None
            for node in range(num_nodes):
                if not visited[node] and shortest_distance[node] < min_distance:
                    min_distance = shortest_distance[node]
                    current_node = node

            if current_node is None:
                break

            visited[current_node] = True

            for prev_node in range(num_nodes):
                if self.cost_matrix[prev_node][current_node] > 0:  # Can be commented for negative-weighted graphs only.
                    new_distance = np.add(shortest_distance[current_node], self.cost_matrix[prev_node][current_node])
                    if new_distance < shortest_distance[prev_node]:
                        shortest_distance[prev_node] = new_distance
                        shortest_path[prev_node] = np.add(shortest_path[current_node], [prev_node])
        if shortest_path[source] is None and shortest_distance[source] == sys.maxsize:
            return [None, None]
        return [shortest_path[source][::-1], shortest_distance[source]]
        # Can also be used to return the shortest path from other nodes to destination node also
        # Now returns a list containing the shortest path with the shortest cost from source to destination node
