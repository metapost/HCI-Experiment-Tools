# Template version
# Modified by haipeng.wang@gmail.com
# v1.0, 20230506, initial release.

## usage guidelines
# assign filename to variable of fn 
# assign pid to current pid number to select his/her row from data
# assign dv to dependent variables to select needed columns from data


# data convert
import csv

fn = 'nasa-rawtlx-results-ccl-v2'

# Open the input file for reading
with open(fn+ '.txt', 'r') as input_file:
    # Read the contents of the file and split each line by commas
    lines = [line.strip().split(' ') for line in input_file.readlines()]

# Open the output file for writing as a CSV file
with open(fn + '.csv', 'w', newline='') as output_file:
    # Create a CSV writer object and write the data to the file
    writer = csv.writer(output_file)
    writer.writerows(lines)

print('Data written to data.csv')


# plot
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(fn + '.csv')

# define the pid to select rows
# define the dv to select columns
pid = 1
dv = ['mental', 'performance', 'effort', 'frustration']

# Select specific rows of pid
df = df.loc[df['pid'] == pid]
print(df)

# Select specific columns by name
columns_to_select = ['condition', 'mental', 'performance', 'effort', 'frustration']
df = df[columns_to_select]
print(df)


# Create the bar chart
num_dv = len(dv)
num_condition = len(df['condition'])

fig, ax = plt.subplots()
width = 0.8 / num_dv # number of dv

for i, var in enumerate(dv):
    x = np.arange(num_condition) + i * width # 2 conditions
    ax.bar(x, df[var], width=width, label=var)

# Set axis labels and title
# ax.set_xlabel('Conditions')
# ax.set_ylabel('Scale')
ax.set_title('Raw TLX')

# Set the x-tick labels
ax.set_xticks(np.arange(num_condition) + 0.4) # 2 conditions
# ax.set_xticklabels(['Condition 1', 'Condition 2'])
ax.set_xticklabels(df['condition'])

# Add a legend
ax.legend()

# Show the plot
plt.show()