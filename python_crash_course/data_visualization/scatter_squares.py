"""
Import matplot libraries required for data visualization sample project.
"""
import matplotlib.pyplot as plt

input_values = list(range(1, 1001))
squares = [x**2 for x in input_values]

plt.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, edgecolors="none", s=40)

# --- SET THE CHART TITLE AND LABEL AXES --- #
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# --- SET SIZE OF TICK LABELS --- #
plt.tick_params(axis="both", which="major", labelsize=14)

# --- SET THE RANGE OF EACH AXIS --- #
plt.axis([0, 1100, 0, 1100000])

# --- SAVE THE PLOT AS AN IMAGE IN THE SAME FOLDER --- #
plt.savefig("squares_plot.png")

# --- DISPLAY THE PLOT --- #
plt.show()
