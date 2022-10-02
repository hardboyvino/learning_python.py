from collections import Counter
import pygal

from die import Die

# --- INITIALIZE A DIE --- #
die_1 = Die()
die_2 = Die(10)
num_of_rolls = 50000

# --- ADD UP 2 INDIVIDUAL DIE ROLLS TOGETHER TO GET COMBINED RESULT --- #
results = [die_1.roll_dice() + die_2.roll_dice() for _ in range(num_of_rolls)]

# --- CREATE A LIST OF ALL POSSIBLE SIDE NUMBERS COMBINATION --- #
die_numbers = list(sorted(set([num_1 + num_2 for num_1 in range(1, die_1.num_sides + 1) for num_2 in range(1, die_2.num_sides + 1)])))

# --- ANALYSE RESULT TO ONLY GET A LIST --- #
frequency = [results.count(value) for value in die_numbers]

# --- RENDER A BAR CHART OF THE RESULTS --- #
bar_chart = pygal.Bar()
bar_chart.title = f"Results from rolling two dice of different sides {num_of_rolls} times"
bar_chart.x_labels = die_numbers
bar_chart.add("Double Dice", frequency)
bar_chart.render_to_file("die_visual_two_dice_diff_sides.svg")
