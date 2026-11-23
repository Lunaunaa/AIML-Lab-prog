
import heapq

goal = (0,1,2,3,4,5,6,7,8)

def heuristic(s):
    h = 0
    for i in range(9):
        if s[i] != 0:
            h += abs(i//3 - s[i]//3) + abs(i%3 - s[i]%3)
    return h

def astar(start):
    pq = [(heuristic(start), 0, start, [start])]
    visited = set()

    while pq:
        f, g, s, path = heapq.heappop(pq)

        if s == goal:
            return path

        if s in visited:
            continue
        visited.add(s)

        p = s.index(0)

        moves = []
        if p >= 3: moves.append(p-3)
        if p < 6: moves.append(p+3)
        if p % 3 != 0: moves.append(p-1)
        if p % 3 != 2: moves.append(p+1)

        for m in moves:
            new = list(s)
            new[p], new[m] = new[m], new[p]
            new = tuple(new)

            if new not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(new)
                heapq.heappush(pq, (new_f, new_g, new, path+[new]))

    return None

start = tuple(map(int, input("Enter 9 numbers: ").split()))

path = astar(start)

if path:
    print("Solution:")
    for s in path:
        for i in range(0, 9, 3):
            print(s[i:i+3])
        print()
    print("Moves:", len(path)-1)
else:
    print("No solution")
