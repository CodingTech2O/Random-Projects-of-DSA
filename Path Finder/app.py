graph = {
    "A": {"B": 6, "C": 3},
    "B": {"A": 6, "C": 2, "D": 5},
    "C": {"A": 3, "B": 2, "D": 3, "E": 7},
    "D": {"B": 5, "C": 3, "E": 2, "F": 4},
    "E": {"C": 7, "D": 2, "F": 1},
    "F": {"D": 4, "E": 1}
}
start = input("Start : ").strip().upper()
end = input("End : ").strip().upper()

found = False
dists = []  # Defined globally so print(dists) works

if start in graph:
    current_loc = start
    reached = graph[current_loc]
    visited = {current_loc}  # Track visited nodes to prevent infinite loops
    dist = 0

    while not found:
        # Filter out nodes we've already visited to avoid looping back
        unvisited_neighbors = {p: d for p, d in reached.items() if p not in visited}
        
        # If no unvisited neighbors remain, stop traversing
        if not unvisited_neighbors:
            print("No unvisited path remaining.")
            break

        # Find the minimum distance among unvisited neighbors
        min_dist = min(unvisited_neighbors.values())
        
        # Identify the next destination based on min_dist
        next_loc = None
        for p, d in unvisited_neighbors.items():
            if d == min_dist:
                next_loc = p
                break

        dist += min_dist
        visited.add(next_loc)
        print(f"Moving from {current_loc} to {next_loc} (distance: {min_dist}, total: {dist})")

        # Check if we reached the target
        if next_loc == end:
            found = True
            dists.append(dist)
            print(f"Reached {end} in total distance {dist}!")
            break

        # Move to the next node's dictionary
        current_loc = next_loc
        reached = graph[current_loc]

print("least distance to travel", min(dists))