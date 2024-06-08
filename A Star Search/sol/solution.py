#BholaTanisha Project1
import heapq

def find_neighbors_and_heuristic(config, target):
    neighbors = []
    manhattan_distance = 0

 # Calculate Manhattan distance for the heuristic
    for num in range(1, 9):  # 0 is the empty space, ignore it
        current_position = config.index(num)
        goal_position = target.index(num)
        current_row, current_col = divmod(current_position, 3)
        goal_row, goal_col = divmod(goal_position, 3)
        manhattan_distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    empty_index = config.index(8)
    empty_row, empty_col = divmod(empty_index, 3)
    potential_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right


# Generate neighbors by moving the empty space (8)
    for move in potential_moves:
        neighbor_row = empty_row + move[0]
        neighbor_col = empty_col + move[1]
        if 0 <= neighbor_row < 3 and 0 <= neighbor_col < 3:
            neighbor_index = neighbor_row * 3 + neighbor_col
            new_config = config[:]
            new_config[empty_index], new_config[neighbor_index] = new_config[neighbor_index], new_config[empty_index]
            neighbors.append((new_config, neighbor_index))

    return neighbors, manhattan_distance

def astar(initial_state):
    target_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    priority_queue = []
    # Push the initial state into the priority queue with its heuristic cost
    heapq.heappush(priority_queue, (0, initial_state))
    path_trace = {}
    g_score = {tuple(initial_state): 0}
    f_score = {tuple(initial_state): find_neighbors_and_heuristic(initial_state, target_state)[1]}

    while priority_queue:
        _, current_state = heapq.heappop(priority_queue)

        # Check if the current state is the goal state
        if current_state == target_state:
            solution_path = []
            while tuple(current_state) in path_trace:
                current_state, move_position = path_trace[tuple(current_state)]
                solution_path.append(move_position)
            solution_path.reverse()
            return solution_path

        # Find neighbors and calculate their heuristic
        neighbors, _ = find_neighbors_and_heuristic(current_state, target_state)
        for neighbor, move in neighbors:
            tentative_g_score = g_score[tuple(current_state)] + 1
            if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                path_trace[tuple(neighbor)] = (tuple(current_state), move)
                g_score[tuple(neighbor)] = tentative_g_score
                heuristic_cost = find_neighbors_and_heuristic(neighbor, target_state)[1]
                #f(s) = g(s) + h(s)
                f_score[tuple(neighbor)] = tentative_g_score + heuristic_cost
                heapq.heappush(priority_queue, (f_score[tuple(neighbor)], neighbor))

    return []

