
# Alpha-Beta Pruning

def alphabeta(level, pos, alpha, beta, isMax):

    if level == depth:
        return values[pos]

    if isMax:
        best = -999

        for i in range(2):
            value = alphabeta(level+1, pos*2+i,
                              alpha, beta, False)

            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

    else:
        best = 999

        for i in range(2):
            value = alphabeta(level+1, pos*2+i,
                              alpha, beta, True)

            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

    return best


# Input leaf values
values = list(map(int, input("Enter leaf values: ").split()))

# Calculate depth automatically
depth = 0
n = len(values)

while n > 1:
    n = n // 2
    depth += 1

result = alphabeta(0, 0, -999, 999, True)

print("Optimal value:", result)
