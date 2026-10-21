# lab 5 maa sir rasikh na minimax aur alpha-beta ka concept dya tha
import math

# Global counters to track how many leaf nodes are evaluated
minimax_leaf_count = 0
alpha_beta_leaf_count = 0

def run_minimax(current_depth, idx, is_max_player, leaf_values, max_depth):
    global minimax_leaf_count
    
    # Base case: reached the bottom (leaf node)
    if current_depth == max_depth:
        minimax_leaf_count += 1
        return leaf_values[idx]
    
    if is_max_player:
        return max(
            run_minimax(current_depth + 1, idx * 2, False, leaf_values, max_depth),
            run_minimax(current_depth + 1, idx * 2 + 1, False, leaf_values, max_depth)
        )
    else:
        return min(
            run_minimax(current_depth + 1, idx * 2, True, leaf_values, max_depth),
            run_minimax(current_depth + 1, idx * 2 + 1, True, leaf_values, max_depth)
        )

def alpha_beta_search(current_depth, idx, is_max_player, leaf_values, max_depth, alpha, beta):
    global alpha_beta_leaf_count
    
    # Base case: reached the bottom (leaf node)
    if current_depth == max_depth:
        alpha_beta_leaf_count += 1
        return leaf_values[idx]
    
    if is_max_player:
        best_val = float('-inf')
        for i in range(2):
            val = alpha_beta_search(current_depth + 1, idx * 2 + i, False, leaf_values, max_depth, alpha, beta)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if alpha >= beta:
                break  # Beta Cutoff (Pruning)
        return best_val
    else:
        best_val = float('inf')
        for i in range(2):
            val = alpha_beta_search(current_depth + 1, idx * 2 + i, True, leaf_values, max_depth, alpha, beta)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if alpha >= beta:
                break  # Alpha Cutoff (Pruning)
        return best_val

def find_best_root_action(leaf_values, max_depth):
    best_val, chosen_action, alpha = float('-inf'), None, float('-inf')
    for i, action_name in enumerate(["Left", "Right"]):
        v = alpha_beta_search(1, i, False, leaf_values, max_depth, alpha, float('inf'))
        if v > best_val:
            best_val, chosen_action = v, action_name
        alpha = max(alpha, best_val)
    return best_val, chosen_action

# Test Cases
test_cases = [
    [3, 5, 2, 9, 3, 5, 2, 9],
    [5, 3, 9, 2, 5, 3, 9, 2],
    [2, 9, 3, 5, 2, 9, 3, 5],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [3, 5, 2, 9, 0, 7, 0, 0],
]

for scores in test_cases:
    minimax_leaf_count = 0
    alpha_beta_leaf_count = 0
    depth = int(math.log2(len(scores)))
    
    print("Scores:", scores)
    print("Minimax Value:", run_minimax(0, 0, True, scores, depth), "| Leaves Evaluated:", minimax_leaf_count)
    print("Alpha-Beta Value:", alpha_beta_search(0, 0, True, scores, depth, float('-inf'), float('inf')), "| Leaves Evaluated:", alpha_beta_leaf_count)
    print("Pruning Successful:", alpha_beta_leaf_count <= minimax_leaf_count)
    
    alpha_beta_leaf_count = 0
    val, act = find_best_root_action(scores, depth)
    print("Root Best Action:", act, "with Value:", val)
    print("-" * 50)

#1.5 ganta laga diff chatbot sa phir jaa kr khud write kya haa
