import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

y = [23, 41, 2, 31, 5, 7, 9, 19, 10, 23, 31, 41]

plt.scatter(x, y, label = "dots", color = "maroon",
            marker = ".", s = 400)

plt.xlabel('Day')

plt.ylabel('Temperature')

plt.title('Daily Temperature')


plt.legend()

plt.show()