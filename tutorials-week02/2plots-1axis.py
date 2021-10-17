# Creating 2 plots on 1 axis by calling plot.plot() twice. 
# Matplotlib remembers the first plot and will add the second.

import matplotlib.pyplot as plt

# Numpy allows to use mathematical functions
import numpy as np

# Determine x and y axis values: 
# Numpy a-range: creates list of numbers between two values. 
# Inclusive of first value, exclusive of second value, last values determines increments
 
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

# Create a list of random values between -1 and 1
# Centre: 0.0, standard deviation: 1.0, size: Length of x-axis
noise = np.random.normal(0.0, 1.0, len(x))


# Plot all as scatter plot with red dots
# Random values of "noise" get added to y values
plt.plot(x, y + noise, 'r.')

# Plot x and y values as a blue line
plt.plot(x, y, 'b-')

plt.show()


# If a second plt.show() is added, when run the program will first display the first plot.
# When that is closed, the program will display the second plot. 

plt.plot(x, y + noise, 'c.')
plt.plot(x, y, 'g-')

plt.show()