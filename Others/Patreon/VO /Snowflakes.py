def normalize_snowflake(snowflake):
    """Find the canonical form of a snowflake by considering all rotations."""
    n = len(snowflake)
    rotations = []

    # Generate all clockwise rotations
    for i in range(n):
        rotations.append(snowflake[i:] + snowflake[:i])

    # Generate all counterclockwise rotations
    for i in range(n):
        rotations.append(snowflake[-i:] + snowflake[:-i])

    # Return the lexicographically smallest rotation
    return min(rotations)

def are_snowflakes_unique(snowflakes):
    """Check if all snowflakes are unique."""
    seen = set()
    for snowflake in snowflakes:
        canonical_form = normalize_snowflake(snowflake)
        snowflake_str = "".join(map(str, canonical_form))
        if snowflake_str in seen:
            return False
        seen.add(snowflake_str)

    return True

# Example Usage
snowflakes = [
    [1, 2, 3, 4, 5, 6],
    [3, 4, 5, 6, 1, 2],
    [6, 1, 2, 3, 4, 5]
]
#print(normalize_snowflake(snowflakes[2]))
print(are_snowflakes_unique(snowflakes))  # Output: False

unique_snowflakes = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
]
print(are_snowflakes_unique(unique_snowflakes))  # Output: True
