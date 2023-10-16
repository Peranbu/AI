import itertools
def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i+1]]
    total_distance += distances[path[-1]][path[0]]  # Return to the starting city
    return total_distance
def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(cities):
        distance = calculate_total_distance(path, distances)
        if distance < shortest_distance:
            shortest_path = path
            shortest_distance = distance
    return shortest_path, shortest_distance
if __name__ == "__main__":
    # Example: Distances between cities
    distances = [
        [0, 29, 20, 21],
        [29, 0, 15, 22],
        [20, 15, 0, 24],
        [21, 22, 24, 0]
    ]
    shortest_path, shortest_distance = traveling_salesman_bruteforce(distances)
    print("Shortest path:", shortest_path)
    print("Shortest distance:", shortest_distance)


#Here’s a more formal definition:
#Given a list of cities and the distances between each pair of cities, find the shortest possible route that visits each city exactly once and returns to the original city.
#It’s important to note that this problem is NP-hard, meaning there is no known algorithm that can solve all instances of the problem quickly (in polynomial time). 
#Therefore, many heuristic methods (approximation algorithms) have been developed to try and solve it in a reasonable amount of time, even though they can’t guarantee an optimal solution. 
#Examples include simulated annealing, genetic algorithms, ant colony optimization algorithms, and more
#The code you’ve written is a Python implementation of the brute force solution to the Traveling Salesman Problem (TSP).

  
#Here’s a step-by-step explanation of the code
#The calculate_total_distance function calculates the total distance of a given path based on the provided distances between cities.
#The traveling_salesman_bruteforce function finds the shortest path that visits all cities and returns to the starting city. It does this by generating all permutations of the cities, calculating the total distance for each permutation, and keeping track of the shortest distance found.
#In the main part of the code, an example set of distances between cities is defined, and then the traveling_salesman_bruteforce function is called to find the shortest path and its distance.
#The output of this code will be the shortest path and its distance.
#Please note that this is a brute force solution, which means it checks all possible paths.
#The time complexity of this solution is O(n!), where n is the number of cities. This makes it impractical for large inputs. 
#There are more efficient algorithms to solve the TSP, but they are also more complex.
