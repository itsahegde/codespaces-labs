import matplotlib.pyplot as plt

def generate_plot(x, y, x_label, y_label, title):
    plt.scatter(x[:, 0], x[:, 1], c = y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
