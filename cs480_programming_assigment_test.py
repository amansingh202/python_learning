#!/usr/bin/env python
# coding: utf-8

# In[18]:


import sys
import csv
import heapq

def load_data():
    # Load driving distances between state capitals
    with open('driving.csv', 'r') as file:
        driving_data = list(csv.reader(file))
    
    # Load straight line distances between state capitals
    with open('straightline.csv', 'r') as file:
        straightline_data = list(csv.reader(file))
    
    return driving_data, straightline_data

def greedy_best_first_search(initial_state, goal_state, driving_data, straightline_data):
    # Create a priority queue to store the states to be explored
    priority_queue = []
    heapq.heappush(priority_queue, (0, [initial_state]))
    
    while priority_queue:
        # Dequeue the state with the highest priority
        _, path = heapq.heappop(priority_queue)
        current_state = path[-1]
        
        if current_state == goal_state:
            return path
        
        print("Current state:", current_state)  # Add this line to check the value of current_state
        
        current_state_index = driving_data[0].index(current_state)
        for neighbor_state, distance in enumerate(driving_data[current_state_index]):
            if distance != '-1':
                # Calculate the heuristic value for the neighbor
                heuristic_value = straightline_data[neighbor_state][straightline_data[0].index(goal_state)]
                priority = heuristic_value
                heapq.heappush(priority_queue, (priority, path + [neighbor_state]))
    
    return None


def a_star_search(initial_state, goal_state, driving_data, straightline_data):
    # Create a priority queue to store the states to be explored
    priority_queue = []
    heapq.heappush(priority_queue, (0, [initial_state]))
    
    while priority_queue:
        # Dequeue the state with the lowest priority
        _, path = heapq.heappop(priority_queue)
        current_state = path[-1]
        
        if current_state == goal_state:
            return path
        
        for neighbor_state, distance in enumerate(driving_data[current_state]):
            if distance != '-1':
                # Calculate the heuristic value for the neighbor
                heuristic_value = int(straightline_data[neighbor_state][goal_state])
                # Calculate the total cost for the neighbor
                total_cost = int(distance) + len(path)
                priority = total_cost
                heapq.heappush(priority_queue, (priority, path + [neighbor_state]))
    
    return None

def main():
    # Read the command line arguments
    if len(sys.argv) != 3:
        print("ERROR: Not enough or too many input arguments.")
        return
    
    goal_state = "CA"
    initial_state = "IL"
    
    # Load and process the input data files
    driving_data, straightline_data = load_data()
    
    # Run Greedy Best First Search
    greedy_path = greedy_best_first_search(initial_state, goal_state, driving_data, straightline_data)
    
    # Run A* Search
    a_star_path = a_star_search(initial_state, goal_state, driving_data, straightline_data)
    
    # Measure the execution time for both algorithms
    
    # Report the results
    print("Last Name, First Name, AXXXXXXXX solution:")
    print("Initial state:", initial_state)
    print("Goal state:", goal_state)
    print()
    print("Greedy Best First Search:")
    if greedy_path:
        print("Solution:", ", ".join(greedy_path))
        print("Number of expanded nodes:", len(greedy_path))
        print("Number of stops on a path:", len(greedy_path) - 1)
        print("Execution time: T1 seconds")
        print("Complete path cost: Y1")
    else:
        print("Solution: NO SOLUTION FOUND")
        print("Number of stops on a path: 0")
        print("Execution time: T3 seconds")
        print("Complete path cost: 0")
    print()
    print("A* Search:")
    if a_star_path:
        print("Solution:", ", ".join(a_star_path))
        print("Number of expanded nodes:", len(a_star_path))
        print("Number of stops on a path:", len(a_star_path) - 1)
        print("Execution time: T2 seconds")
        print("Complete path cost: Y2")
    else:
        print("Solution: NO SOLUTION FOUND")
        print("Number of stops on a path: 0")
        print("Execution time: T3 seconds")
        print("Complete path cost: 0")

if __name__ == "__main__":
    main()

