from collections import Counter
import pygal

from die import Die

# --- INITIALIZE A DIE --- #
die = Die()
num_of_rolls = 10000

# --- CREATE A LIST OF RANDOM DIE ROLLS, NUMBER OF ROLLS SPECIFIED MANUALLY --- #
results = [die.roll_dice() for _ in range(num_of_rolls)]

# --- CREATE A LIST OF ALL POSSIBLE SIDE NUMBERS --- #
die_numbers = sorted([num for num in range(1, die.num_sides + 1)])

# --- ANALIZE THE RESULT OF ROLLS TO GET A DICTIONARY --- #
c = Counter(results)
c = {key:val for key, val in sorted(c.items(), key=lambda x:x[0])}

# --- METHOD 2 FOR ANALYSE RESULT TO ONLY GET A LIST --- #
frequency = [results.count(value) for value in range(1, die.num_sides + 1)]

# --- RENDER A BAR CHART OF THE RESULTS --- #
bar_chart = pygal.Bar()
bar_chart.title = f"Results from rolling one die {num_of_rolls} times"
bar_chart.x_labels = die_numbers
bar_chart.add("Single Die", frequency)
bar_chart.render_to_file("die_visual.svg")
