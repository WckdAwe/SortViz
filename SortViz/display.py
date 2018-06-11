from matplotlib import pyplot as plt

plt.style.use('bmh')
plt.ion()


def display(a, fig):
    if not fig:
        return

    plt.clf()

    plt.bar(range(len(a)), a)
    plt.draw()
    plt.pause(0.05)
    if plt.fignum_exists(fig.number):
        print("Window still open")
    else:
        print("Window closed")
        return -1
