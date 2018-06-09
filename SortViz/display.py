from matplotlib import pyplot as plt
import matplotlib
from time import sleep

plt.style.use('bmh')
plt.ion()


def display(a, fig):
	# print(fig.number)
	plt.clf()

	plt.bar(range(len(a)),a)
	plt.draw()
	plt.pause(0.05)
	if plt.fignum_exists(fig.number):
		print("Window still open")
	else:
		print("Window closed")
		return -1


