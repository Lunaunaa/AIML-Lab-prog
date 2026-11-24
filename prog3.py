#installation:python -m pip install heapq
import heapq

goal = (0,1,2,3,4,5,6,7,8)

# Calculate heuristic
def h(s):
    count = 0
    for i in range(9):
        if s[i] != 0:
            count += abs(i//3 - s[i]//3) + abs(i%3 - s[i]%3)
    return count

# A* algorithm
def astar(start):
    pq = [(h(start), 0, start, [start])]
    visited = set()

    while pq:
        f, g, s, path = heapq.heappop(pq)

        if s == goal:
            return path

        if s in visited:
            continue

        visited.add(s)

        pos = s.index(0)
        moves = []

        if pos >= 3:
            moves.append(pos-3)
        if pos < 6:
            moves.append(pos+3)
        if pos % 3 != 0:
            moves.append(pos-1)
        if pos % 3 != 2:
            moves.append(pos+1)

        for m in moves:
            new = list(s)
            new[pos], new[m] = new[m], new[pos]
            new = tuple(new)

            if new not in visited:
                heapq.heappush(pq, (g+1+h(new), g+1, new, path+[new]))

    return None

# Input
start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))

path = astar(start)

if path:
    print("Solution:")
    for s in path:
        for i in range(0, 9, 3):
            print(s[i:i+3])
        print()
    print("Total moves:", len(path)-1)
else:
    print("No solution")
