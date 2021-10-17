# Adding titles, legends and labels to plots

import matplotlib.pyplot as plt
import numpy as np

 
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))

# Adding labels to display in the legend
plt.plot(x, y + noise, 'r.', label="Actual")
plt.plot(x, y, 'b-', label="Model")

# plt.title() adds a title
plt.title("Tadaaaa, a plot!")

# plt.xlabel() / plt.ylabel() adds labels to the x and y axes
plt.xlabel("x values")
plt.ylabel("y values")

# plt.legend() adds a legend, labels for each individual plot are required
plt.legend()

plt.show()

# Can also add a grid, different ticks and sub-ticks to axes or LaTex formatting https://www.latex-project.org/about/ 