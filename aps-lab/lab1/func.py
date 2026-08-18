from data import gen_linear_data, gen_nonlinear_data
from visual import generate_plot

x, y = gen_nonlinear_data(101)
generate_plot(x, y, "x", "y", "Plot")