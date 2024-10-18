# Kaiqi's solution
# Cause there may be repeating blocks, use a set to track the block, and while looping over the operations, check whether there is a block in the range[x-(size-1), x+(size-1)]
# Good that I came up with the idea of using flag variables, though the GPT gives anotehr neater way of solving this.

def solution1(operations):
    obstacles = set()
    res = []

    for operation in operations:
        if operation[0] == 1:
            obstacles.add(operation[1])
        else:
            type, center, size = operation
            hasBlock = False #  flag vairable
            for i in range(center - (size-1), center+(size-1)+1):
                if i in obstacles:
                    hasBlock = True
                    res.append("0")
                    break
                else:
                    continue
            if not hasBlock:
                res.append("1")
    return "".join(res)

# GPTSolution
def solution2(operations):
    
    # Set to store obstable position
    obstacles = set()
    res = []
    
    # process each operation
    for operation in operations:
        if operation[0] == 1:
            # Add an obstacle at the given position
            obstacles.add(operation[1])
        elif operation[0] == 2:
            # get the center position and size
            x, size = operation[1], operation[2]
            
            # Calculate the range o check for obstacles
            left_bound = x - (size-1)
            right_bound = x + (size-1)
            
            # Check any obstacles in the range
            can_build = True
            for i in range(left_bound, right_bound+1):
                if i in obstacles:
                    can_build = False
                    break
            res.append("1" if can_build else "0")
    return "".join(res)
        
    # Result for type 2 operation 
if __name__ == "__main__":
    operations = [[1, 2], [1, 6], [2, 4, 2], [2, 5, 2], [2, 1, 1], [2, 1, 2]]
    print(solution2(operations))
                
            

    