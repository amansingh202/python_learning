#!/usr/bin/env python
# coding: utf-8

# In[18]:


import sys
import queue
import time
import pandas as pd

class Node:
    def __init__(self, state, path_cost):
        self.state = state
        self.path_cost = path_cost

class Problem:
    def __init__(self, initial_state, goal_state, graph, heuristics):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = graph
        self.heuristics = heuristics

    def is_goal(self, state):
        return state == self.goal_state

    def expand(self, node):
        children = []
        if node.state in self.graph:
            for neighbor, distance in self.graph[node.state]:
                child = Node(state=neighbor, path_cost=node.path_cost + distance)
                children.append(child)
        return children

def heuristic(state, heuristics):
    return heuristics[state]

def greedy_best_first_search(problem):
    frontier = queue.PriorityQueue()
    frontier.put((problem.heuristics[problem.initial_state], Node(problem.initial_state, 0)))  
    reached = {problem.initial_state: Node(problem.initial_state, 0)}
    expanded_nodes = 0

    while not frontier.empty():
        _, node = frontier.get()
        expanded_nodes += 1
        if problem.is_goal(node.state):
            return node, expanded_nodes
        for child in problem.expand(node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.put((problem.heuristics[s], child))

    return None, expanded_nodes  

def astar(problem):
    frontier = queue.PriorityQueue()
    frontier.put((0 + problem.heuristics[problem.initial_state], Node(problem.initial_state, 0)))  
    reached = {problem.initial_state: Node(problem.initial_state, 0)}
    expanded_nodes = 0

    while not frontier.empty():
        _, node = frontier.get()
        expanded_nodes += 1
        if problem.is_goal(node.state):
            return node, expanded_nodes
        for child in problem.expand(node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.put((child.path_cost + problem.heuristics[s], child))

    return None, expanded_nodes  

def read_driving_distances(file_path):
    graph = {}
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        source = row['Source']  
        if source not in graph:
            graph[source] = []
        graph[source].append((row['Destination'], row['Distance']))  
    return graph

def read_heuristics(file_path):
    heuristics = {}
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        heuristics[row['State']] = row['Heuristic']
    return heuristics

def run_algorithm(algorithm, problem):
    start_time = time.time()
    result, expanded_nodes = algorithm(problem)
    execution_time = time.time() - start_time
    if result:
        path = [node.state for node in result]
        path_cost = result.path_cost
        return path, expanded_nodes, execution_time, path_cost
    else:
        return None, expanded_nodes, execution_time, 0

def main():
    if len(sys.argv) != 3:
        print("ERROR: Not enough or too many input arguments.")
        sys.exit(1)

    goal_state = sys.argv[1]
    initial_state = sys.argv[2]

    graph = read_driving_distances('driving.csv')
    heuristics = read_heuristics('straightline.csv')

    problem = Problem(initial_state, goal_state, graph, heuristics)

    # Run Greedy Best First Search
    gbfs_results = []
    for _ in range(10):
        gbfs_result = run_algorithm(greedy_best_first_search, problem)
        gbfs_results.append(gbfs_result)

    # Run A* Algorithm
    astar_results = []
    for _ in range(10):
        astar_result = run_algorithm(astar, problem)
        astar_results.append(astar_result)

    # Calculate averages
    gbfs_expanded_avg = sum(result[1] for result in gbfs_results) / len(gbfs_results)
    gbfs_time_avg = sum(result[2] for result in gbfs_results) / len(gbfs_results)
    astar_expanded_avg = sum(result[1] for result in astar_results) / len(astar_results)
    astar_time_avg = sum(result[2] for result in astar_results) / len(astar_results)

    # Print results
    print(f"Last Name, First Name, AXXXXXXXX solution:")
    print(f"Initial state: {initial_state}")
    print(f"Goal state: {goal_state}\n")

    print("Greedy Best First Search:")
    for i, result in enumerate(gbfs_results):
        path = result[0] if result[0] else "NO SOLUTION FOUND"
        print(f"Solution: {', '.join(path)}")
        print(f"Number of expanded nodes: {result[1]}")
        print(f"Execution time: {result[2]} seconds")
        print(f"Complete path cost: {result[3]}\n")

    print("A* Search:")
    for i, result in enumerate(astar_results):
        path = result[0] if result[0] else "NO SOLUTION FOUND"
        print(f"Solution: {', '.join(path)}")
        print(f"Number of expanded nodes: {result[1]}")
        print(f"Execution time: {result[2]} seconds")
        print(f"Complete path cost: {result[3]}\n")

    # Print averages
    print("Averages:")
    print(f"Greedy Best First Search - Expanded Nodes: {gbfs_expanded_avg}")
    print(f"Greedy Best First Search - Execution Time: {gbfs_time_avg} seconds")
    print(f"A* Search - Expanded Nodes: {astar_expanded_avg}")
    print(f"A* Search - Execution Time: {astar_time_avg} seconds")

if __name__ == "__main__":
    main()

