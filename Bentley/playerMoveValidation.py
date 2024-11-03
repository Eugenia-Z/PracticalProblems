# The whole idea of this problem is just to translate the requirement to working code. No fancy data structured involved.
# One Pass solution to iterate the string with a boolean array marking the status. 
def solution(S):
    n = len(S)
    successful_moves = 0
    
    # A boolean array to track which fields are "blocked" by players
    occupied = [True] * n
    
    # Traverse players from left to right to determine valid moves
    for i in range(n):
        move = S[i]
        
        if move == '>':
            if i == n-1 or (i+1 < n and not occupied[i+1]):
                successful_moves += 1
                if i < n-1:
                    # update only if it's not the last player
                    occupied[i+1] = True
                occupied[i] = False
        elif move == '<':
            if i == 0 or (i-1 >= 0 and not occupied[i-1]):
                successful_moves += 1
                if i > 0:
                    # update only if it's not the first player
                    occupied[i-1] = True
                occupied[i] = False

        elif move == '^' or move == 'v': 
            # Vertical moves are always successful and they're not blocking anyone
            successful_moves += 1
            occupied[i] = False
    return successful_moves

# Example usage
print(solution("<<^<v>>"))

                 