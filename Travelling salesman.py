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



