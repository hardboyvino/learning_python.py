"""
Import matplot libraries required for data visualization sample project.
"""
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=3)

# --- SET THE CHART TITLE AND LABEL AXES --- #
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# --- SET SIZE OF TICK LABELS --- #
plt.tick_params(axis="both", labelsize=14)

# --- DISPLAY THE PLOT --- #
plt.show()
