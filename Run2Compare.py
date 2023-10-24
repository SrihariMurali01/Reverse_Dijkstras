import time
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

# Import Runner from the Runner module
from Runner import Runner
from djikstras import Dj as dj

# Set OMP_NUM_THREADS to the number of CPU threads available in the system - enables multiprocessing for numpy arrays
os.environ["OMP_NUM_THREADS"] = str(os.cpu_count())

def find_shortest_path(cost_matrix, source, destination):
    # Create a Runner instance with the given cost matrix
    ob = Runner(cost_matrix)
    # Call the find_shortest_path method from the Runner class
    return ob.find_shortest_path(source=source, destination=destination)

def dijkstra_shortest_path(cost_matrix, source, destination):
    # Use NetworkX to calculate the shortest path and return the result
    ob = dj(cost_matrix)
    return ob.find_shortest_path(source=source, destination=destination)

def generate_cost_matrix(size):
    cost_matrix = [[random.randint(1, 100) if i != j else 0 for j in range(size)] for i in range(size)]
    return cost_matrix

def main():
    iterations = int(input('Enter the number of iterations required: '))  # Number of iterations for each size
    x = int(input('Enter the range of sizes of the cost matrix needed, multiples of 5: '))
    sizes = [i for i in range(5, x+1, 5)]  # Vary the cost matrix sizes as needed
    case_type = "custom"  # Specify the type of cost matrix

    your_algorithm_times = []  # List to store execution times for your algorithm
    dijkstra_times = []  # List to store execution times for Dijkstra's algorithm

    for size in sizes:
        your_algorithm_time_for_size = []  # List to store execution times for your algorithm for this size
        dijkstra_time_for_size = []  # List to store execution times for Dijkstra's algorithm for this size

        for i in tqdm(range(iterations), desc=f"Analyzing time complexity: {size}-{case_type}"):
            cost_matrix = generate_cost_matrix(size)
            source_node = 0
            destination_node = size - 1  # Always the final node.

            # Measure time for your algorithm
            start_time = time.time()
            find_shortest_path(cost_matrix, source_node, destination_node)
            end_time = time.time()
            your_algorithm_time_for_size.append(end_time - start_time)

            # Measure time for Dijkstra's algorithm
            start_time = time.time()
            dijkstra_shortest_path(cost_matrix, source_node, destination_node)
            end_time = time.time()
            dijkstra_time_for_size.append(end_time - start_time)

        your_algorithm_times.append(sum(your_algorithm_time_for_size) / iterations)
        dijkstra_times.append(sum(dijkstra_time_for_size) / iterations)

    # Create two separate graphs
    plt.figure(figsize=(12, 6))

    # Your Algorithm Graph
    plt.subplot(1, 2, 1)
    plt.plot(sizes, your_algorithm_times, label="Proposed Algorithm", color='red')
    plt.xlabel("Graph Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Your Algorithm Time Complexity")
    plt.legend()
    plt.gca().set_yticklabels([])

    # Dijkstra's Algorithm Graph
    plt.subplot(1, 2, 2)
    plt.plot(sizes, dijkstra_times, label="Dijkstra's Algorithm")
    plt.xlabel("Graph Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Dijkstra's Algorithm Time Complexity")
    plt.legend()
    plt.gca().set_yticklabels([])  # Disable y-axis labels

    plt.tight_layout()  # Ensure proper spacing between subplots
    plt.show()

if __name__ == "__main__":
    main()
