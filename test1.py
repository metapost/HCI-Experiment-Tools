import matplotlib.pyplot as plt
from appJar import gui

# Create a new GUI object
app = gui()

# Define a function to show the plot
def show_plot(tab):
    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    
    # Plot some data on the axes
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    ax.plot(x, y)
    
    # Show the plot
    plt.show()

# Add a new tab to the GUI
app.addTab("Plot")

# Add a button to the tab to show the plot
app.addButton("Show Plot", show_plot)

# Start the GUI
app.go()
