import numpy as np

def interpolate_trajectory(x_coords, y_coords, dx=0.1):
    # Initialize lists for interpolated trajectory
    new_x_coords = []
    new_y_coords = []
    
    # Initialize the first point in the trajectory
    new_x_coords.append(round(x_coords[0] / dx) * dx)
    new_y_coords.append(y_coords[0])
    
    # Loop through each segment of the original trajectory
    for i in range(1, len(x_coords)):
        # Calculate the step in x and y between current and next point
        x_start = x_coords[i-1]
        x_end = x_coords[i]
        y_start = y_coords[i-1]
        y_end = y_coords[i]
        
        # Interpolate y values for every new x point with dx step
        x_curr = new_x_coords[-1]
        while x_curr + dx <= x_end:
            x_curr += dx
            new_x_coords.append(x_curr)
            # Linear interpolation for y value
            y_interp = y_start + (x_curr - x_start) * (y_end - y_start) / (x_end - x_start)
            new_y_coords.append(y_interp)
    
    return np.array(new_x_coords), np.array(new_y_coords)

# Example trajectory (continuous x and y)
x_coords = [0.12, 0.18, 0.29, 0.35, 0.42]
y_coords = [1, 2, 1.5, 3, 2.5]

# Interpolate the trajectory to a grid with dx = 0.1
new_x, new_y = interpolate_trajectory(x_coords, y_coords)

# Output new interpolated values
print("New x:", new_x)
print("New y:", new_y)
