import math

leaves_mm = 0
leaves_ab = 0

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global leaves_mm
    if curDepth == targetDepth:
        leaves_mm = leaves_mm + 1
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global leaves_ab
    if depth == target:
        leaves_ab = leaves_ab + 1
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

tests = [
    [3, 5, 2, 9, 3, 5, 2, 9],
    [5, 3, 9, 2, 5, 3, 9, 2],
    [2, 9, 3, 5, 2, 9, 3, 5],
    [4, 4, 4, 4, 4, 4, 4, 4]
]

for s in tests:
    leaves_mm = 0
    leaves_ab = 0
    d = int(math.log2(len(s)))
    print("Scores:", s)
    print("Minimax:", minimax(0, 0, True, s, d), "Leaves:", leaves_mm)
    print("AlphaBeta:", alphabeta(0, 0, True, s, d, float('-inf'), float('inf')), "Leaves:", leaves_ab)
    print()