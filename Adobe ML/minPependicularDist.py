import numpy as np
def find_min_distance_point(points, a, b, c):
    
    # Calculate perpendicular distances from each point to the line ax + by + c = 0
    distances = np.abs(a*points[:,0] + b*points[:,1] + c) / np.sqrt(a**2 + b**2)
    
    # Find the index of the point with the minimum disance
    min_index = np.argmin(distances)
    
    # Return the point with the minimum distance
    return points[min_index]

if __name__ == "__main__":
    points = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    a, b, c = 1, -1, -3
    min_distance_point = find_min_distance_point(points, a, b, c)
    print(min_distance_point)