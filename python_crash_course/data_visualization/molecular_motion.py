"""
Visualize the random walks.
"""
import matplotlib.pyplot as plt

from random_walks import RandomWalks


# --- KEEP MAKING WALKS AS LONG AS THE PROGRAM IS ACTIVE --- #
while True:
    # --- MAKE A RANDOM WALK, PLOT THE POINTS --- #
    random_walk = RandomWalks()
    random_walk.fill_walk()

    # --- CREATE A LIST FOR THE NUMBER OF POINTS --- #
    point_numbers = list(range(random_walk.num_points))

    # --- DEFAULT SIZE FOR EVERY PLOT --- #
    plt.figure(figsize=(10.0, 7.5), dpi=120)

    # --- THE LINE PLOT --- #
    plt.plot(random_walk.x_values, random_walk.y_values, linewidth=1)

    # --- HIGHLIGHT THE FIRST AND LAST POINT IN THE RANDOM WALK --- #
    plt.scatter(0, 0, c="green", s=100, edgecolors="none")
    plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c="red", s=100, edgecolors="none")
    # plt.savefig("random_walks.png")

    # --- REMOVE THE AXES --- #
    plt.axis("off")

    # --- PLOT TITLE AND SHOW --- #
    plt.title("Random Walks")
    plt.show()

    # --- PROMPT FOR ANOTHER RANDOM WALK --- #
    keep_running = (input("Make another walk? (y/n): ")).lower()
    if keep_running == "n":
        break
