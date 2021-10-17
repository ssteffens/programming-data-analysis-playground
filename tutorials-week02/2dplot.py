# Tutorial: https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# To use pyplot, it needs to be installed and imported into the program
# If Anaconda is installed matplotlib packacke will be included, if not needs to be installed separately

# adding "as plt" enables to use a short name instaed of having to type the whole name "matplotlib.pyplot.plot()"

import matplotlib.pyplot as plt

""" 
# 1. Basic line plot
# plt.plot() creates a new plot:
# Python uses the values in the list as y values. If no values entered for x values, by default it starts a new list which always start with 0
# so the plot printed has x-values 0, 1, 2, 3
# By default, pyplot plots a line rather than points
plt.plot([1, 2, 3, 4])

# plt.ylabel() adds description to y axis:
plt.ylabel("Some numbers")

# plt.show() displays the plot created
plt.show()
"""


# 2. Scatter plot of square numbers
# To determine values for x-axis, enter a second list
# Adding 'b' changes colour to blue, adding '.' changes plot to scatter plot (dots)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], '.')

plt.ylabel("Square numbers")

plt.show()

