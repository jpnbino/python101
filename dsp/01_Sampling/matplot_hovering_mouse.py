import matplotlib.pyplot as plt
import numpy as np

# Generate example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
fig, ax = plt.subplots()
line, = ax.plot(x, y, 'o', picker=5)  # picker=5 specifies the tolerance for mouse selection

# Function to display the value of the selected point
def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    point = (xdata[ind], ydata[ind])
    ax.annotate(f'x={point[0]:.2f}\ny={point[1]:.2f}', xy=point, xycoords='data',
                xytext=(-30,30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3,rad=.2"))
    fig.canvas.draw_idle()

# Connect the function to the plot
fig.canvas.mpl_connect('pick_event', onpick)

plt.show()
