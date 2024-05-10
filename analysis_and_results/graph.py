from cmath import log

import matplotlib.pyplot as plt
import pandas as pd

# List of CSV files to read
file_list = ['hungarian.csv', 'greedy.csv']

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(12, 6))

# Loop through each file
for file in file_list:
    # Read the CSV file
    data = pd.read_csv(file)

    # Extract the relevant columns
    grid_size = data['grid size']
    #time_taken = data['time taken for matching(in microseconds)']
    steps = data['steps']
    for i in range(len(steps)):
        if steps[i] != 0:
            steps[i] = log(steps[i])
    # Plot the data
    ax.plot(grid_size, steps, marker='o', label=file.split('.')[0])

# Set axis labels and title
ax.set_xlabel('Grid Size', fontsize=14)
ax.set_ylabel('no of steps', fontsize=14)
ax.set_title('Algorithm Performance Comparison', fontsize=16)

# Rotate x-axis labels and adjust font size
plt.xticks(rotation=45, fontsize=8)

# Add a legend
ax.legend()

# Show the grid
ax.grid(True)

# Adjust spacing between subplots
plt.subplots_adjust(bottom=0.2)

# Show the plot
plt.show()