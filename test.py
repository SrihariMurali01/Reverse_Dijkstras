from Runner import Runner


def sssp_algorithm(graph, source, destination):
    r = Runner(graph)
    return r.find_shortest_path(source, destination)


# Test case 1: Simple graph with positive edge weights
graph1 = [
    [0, 2, 1, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 4],
    [0, 0, 0, 0],
]
source1 = 0
destination1 = 3
expected_result1 = [[0, 1, 3], 5]

# Test case 2: Another simple graph with positive edge weights
graph2 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 4, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
]
source2 = 0
destination2 = 4
expected_result2 = [[0, 1, 3, 4], 6]

# Test case 3: Unreachable destination
graph3 = [
    [0, 2, 1, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 4],
    [0, 0, 0, 0],
]
source3 = 0
destination3 = 6
expected_result3 = [None, None]  # Invalid input

# # Test case 4: Negative edge weights - This works when the edit is done in Runner()
# graph4 = [
#     [0, -2, 1, 0],
#     [0, 0, 0, -3],
#     [0, 0, 0, 4],
#     [0, 0, 0, 0],
# ]
# source4 = 0
# destination4 = 3
# expected_result4 = [[0, 1, 3], -5]

# Test case 5: Empty graph
graph5 = []
source5 = 0
destination5 = 1
expected_result5 = [None, None]  # Invalid input

# Test case 6: Single-node graph
graph6 = [[0]]
source6 = 0
destination6 = 0
expected_result6 = [[0], 0]

# Test case 7: Negative cycle
graph7 = [
    [0, 2, 1],
    [0, 0, -3],
    [0, 0, 0],
]
source7 = 1
destination7 = 2
expected_result7 = [None, None]  # Negative cycle

# Test case 8: Disconnected graph
graph8 = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
]
source8 = 0
destination8 = 3
expected_result8 = [None, None]

# Test case 9: Large graph
# Test case 9: Large graph
graph9 = [[0] * 100 for _ in range(100)]
source9 = 0
destination9 = 99
expected_result9 = [None, None]   # No path

# Test case 10: Loop in the graph
graph10 = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
]
source10 = 0
destination10 = 3
expected_result10 = [[0, 1, 2, 3], 3]

graph11 = [
    [0, 3, 2, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
source11 = 0
destination11 = 4
expected_result11 = [[0, 2, 4], 6]

# Run the test cases
test_cases = [
    (graph1, source1, destination1, expected_result1),
    (graph2, source2, destination2, expected_result2),
    (graph3, source3, destination3, expected_result3),
    # (graph4, source4, destination4, expected_result4),
    (graph5, source5, destination5, expected_result5),
    (graph6, source6, destination6, expected_result6),
    (graph7, source7, destination7, expected_result7),
    (graph8, source8, destination8, expected_result8),
    (graph9, source9, destination9, expected_result9),
    (graph10, source10, destination10, expected_result10),
    (graph11, source11, destination11, expected_result11)
]

for i, (graph, source, destination, expected_result) in enumerate(test_cases):
    result = sssp_algorithm(graph, source, destination)
    print(result)
    if result == expected_result:
        print(f"Test case {i + 1}: Passed")
    else:
        print(f"Test case {i + 1}: Failed. Expected {expected_result}, but got {result}")

#
# Number of Cost Matrices generated: 150000
# Time taken: 00:08:00

