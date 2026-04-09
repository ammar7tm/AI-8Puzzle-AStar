import heapq

# A* 8 Puzzle Solver
# Ammar Ismail

# Goal state
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Example initial state
initial_state = (2, 8, 3,
                 1, 6, 4,
                 7, 0, 5)
# Function to print the puzzle
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

# Function to find the blank tile
def find_blank(state):
    return state.index(0)

# Function to generate possible moves
def get_possible_moves(state):
    blank = find_blank(state)
    moves = []

    if blank not in [0, 1, 2]:  # up
        moves.append(blank - 3)

    if blank not in [6, 7, 8]:  # down
        moves.append(blank + 3)

    if blank not in [0, 3, 6]:  # left
        moves.append(blank - 1)

    if blank not in [2, 5, 8]:  # right
        moves.append(blank + 1)

    return moves

# Function to swap blank with another tile
def make_move(state, new_blank):
    blank = find_blank(state)
    state_list = list(state)
    state_list[blank], state_list[new_blank] = state_list[new_blank], state_list[blank]
    return tuple(state_list)

# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goal_index = GOAL_STATE.index(tile)

            current_row = i // 3
            current_col = i % 3

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance

# Misplaced tiles heuristic
def misplaced_tiles(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL_STATE[i]:
            count += 1

    return count

# A* search using Manhattan distance
def a_star(start_state):
    priority_queue = []
    visited = set()

    # (f, g, state, path)
    start_h = manhattan_distance(start_state)
    heapq.heappush(priority_queue, (start_h, 0, start_state, [start_state]))

    nodes_explored = 0

    while priority_queue:
        f, g, current_state, path = heapq.heappop(priority_queue)

        if current_state in visited:
            continue

        visited.add(current_state)
        nodes_explored += 1

        if current_state == GOAL_STATE:
            return path, nodes_explored

        for move in get_possible_moves(current_state):
            new_state = make_move(current_state, move)

            if new_state not in visited:
                new_g = g + 1
                new_h = manhattan_distance(new_state)
                new_f = new_g + new_h

                heapq.heappush(priority_queue, (new_f, new_g, new_state, path + [new_state]))

    return None, nodes_explored

# Run the solver
solution_path, nodes_explored = a_star(initial_state)

print("Initial State:")
print_state(initial_state)

if solution_path is not None:
    print("Solution found!")
    print("Number of moves:", len(solution_path) - 1)
    print("Nodes explored:", nodes_explored)
    print()

    print("Solution path:")
    for state in solution_path:
        print_state(state)
else:
    print("No solution found.")