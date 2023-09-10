import time
import random
import matplotlib.pyplot as plt
from Runner import Runner
from tqdm import tqdm
import os

# # Set OMP_NUM_THREADS to no. of cpu threads available in the system - enables multiprocessing for numpy arrays
# os.environ["OMP_NUM_THREADS"] = str(os.cpu_count())


# Algorithm implementation (replace with your implementation)

def find_shortest_path(cost_matrix, source, destination):
    # Generate random cost matrix for worst, average, and best cases
    ob = Runner(cost_matrix)
    return ob.find_shortest_path(source=source, destination=destination)


def generate_cost_matrix(size, case_type):
    if case_type == "worst":
        cost_matrix = [[random.randint(1, 100) if i != j else 0 for j in range(size)] for i in range(size)]
    elif case_type == "average":
        cost_matrix = [[random.randint(0, 20) if i != j else 0 for j in range(size)] for i in range(size)]
    elif case_type == "best":
        cost_matrix = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                cost_matrix[i][j] = random.randint(1, 10)
                cost_matrix[j][i] = cost_matrix[i][j]
    return cost_matrix


def main():
    iterations = int(input('Enter the number of iterations required: '))  # Number of iterations for each size and case
    x = int(input('Enter the range of sizes of cost matrix needed, multiples of 5: '))
    sizes = [i for i in range(5, x+1, 5)]  # Vary the cost matrix sizes as needed
    cases = ["best", "average", "worst"]

    for case_type in cases:
        avg_times = []
        for size in sizes:
            total_time = 0

            for i in tqdm(range(iterations), desc=f"Plotting time complexity analysis: {size}-{case_type}"):
                cost_matrix = generate_cost_matrix(size, case_type)
                source_node = 0
                destination_node = size - 1  # Always final node.

                start_time = time.time()
                find_shortest_path(cost_matrix, source_node, destination_node)
                end_time = time.time()

                total_time += end_time - start_time

            avg_time = total_time / iterations
            avg_times.append(avg_time)

        plt.plot(sizes, avg_times, label=case_type)

    plt.xlabel("Graph Size")
    plt.ylabel("Average Time (ms)")
    plt.title("Algorithm Time Complexity Analysis")
    plt.legend()
    plt.show()

    return len(sizes) * iterations * len(cases)


def convert(n):
    return time.strftime("%H:%M:%S", time.gmtime(n))


if __name__ == "__main__":
    start = time.time()
    gen = main()
    print(f"Number of Cost Matrices generated: {gen}")
    end = time.time()
    print(f"Time taken: {convert(end - start)}")
