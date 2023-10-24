import heapq



class Node:

    def __init__(self, x, y, parent=None):

        self.x = x

        self.y = y

        self.parent = parent

        self.g = 0

        self.h = 0



    def __lt__(self, other):

        return (self.g + self.h) < (other.g + other.h)



def heuristic(node, goal):

    return abs(node.x - goal.x) + abs(node.y - goal.y)



def astar(grid, start, goal):

    open_set = []

    closed_set = set()

    start_node = Node(start[0], start[1])

    goal_node = Node(goal[0], goal[1])

    heapq.heappush(open_set, start_node)



    while open_set:

        current_node = heapq.heappop(open_set)



        if current_node.x == goal_node.x and current_node.y == goal_node.y:

            path = []

            while current_node:

                path.append((current_node.x, current_node.y))

                current_node = current_node.parent

            return path[::-1]



        closed_set.add((current_node.x, current_node.y))



        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            new_x, new_y = current_node.x + dx, current_node.y + dy



            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:

                if (new_x, new_y) not in closed_set:

                    child_node = Node(new_x, new_y, parent=current_node)

                    child_node.g = current_node.g + 1

                    child_node.h = heuristic(child_node, goal_node)

                    heapq.heappush(open_set, child_node)



    return None



if __name__ == "__main__":

    # Example grid (0 represents empty, 1 represents an obstacle)

    grid = [

        [0, 0, 0, 0, 0],

        [0, 1, 1, 0, 0],

        [0, 1, 0, 0, 0],

        [0, 1, 0, 1, 0],

        [0, 0, 0, 0, 0]

    ]



    start = (0, 0)

    goal = (4, 4)



    path = astar(grid, start, goal)

    if path:

        print("Path found:", path)

    else:

        print("No path found.")



