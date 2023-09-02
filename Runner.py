import sys


class Runner:

    def __init__(self, cost_matrix):
        self.cost_matrix = cost_matrix

    def find_shortest_path(self, source, destination):
        num_nodes = len(self.cost_matrix)
        visited = [False] * num_nodes
        shortest_distance = [sys.maxsize] * num_nodes
        shortest_path = [[] for _ in range(num_nodes)]

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
                    new_distance = shortest_distance[current_node] + self.cost_matrix[prev_node][current_node]
                    if new_distance < shortest_distance[prev_node]:
                        shortest_distance[prev_node] = new_distance
                        shortest_path[prev_node] = shortest_path[current_node] + [prev_node]

        return [shortest_path[source][::-1], shortest_distance[source]]
        # Can also be used to return the shortest path from other nodes to destination node also
        # Now returns a list containing the shortest path with the shortest cost from source to destination node
