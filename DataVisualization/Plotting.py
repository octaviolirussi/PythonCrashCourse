# import  matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1,4,9,16,25]

# plt.style.use('seaborn-v0_8-dark')

# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)

# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# ax.tick_params(axis='both', labelsize=14)

# fig.show(True)
# input("Presiona ENTER para cerrar...")

#-----------------------------------------------------------------------------------------------------------------#

#Plotting a Series of Points with scatter()#

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

fig.show(True)
input("Presiona ENTER para cerrar...")
