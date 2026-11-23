
# Alpha-Beta Pruning

def alphabeta(level, pos, alpha, beta, isMax):

    if level == 3:
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

        return best

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


# Input leaf node values
values = list(map(int, input("Enter 8 leaf values: ").split()))

result = alphabeta(0, 0, -999, 999, True)

print("Optimal value:", result)
