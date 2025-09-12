# import matplotlib.pyplot as plt

# from RandomWalks import RandomWalk

# rw = RandomWalk()
# rw.fill_walk()

# # Plot the points in the walk.
# plt.style.use('seaborn-v0_8-dark')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()
# input("Presiona ENTER para cerrar...")

#-----------------------------------------------------------------------------------------------------------#

#Rolling the Die#

from RollingDice import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6.
die = Die()
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')