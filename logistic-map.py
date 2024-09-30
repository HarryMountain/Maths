from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

x = 0
k = 0


def values(x, k):
    x_vals = np.array([x])
    for i in range(200):
        x = k*x*(1-x)
        x_vals = np.append(x_vals, x)
    return x_vals


x_vals = values(x, k)


x_points = np.array(range(201))
fig = plt.figure()
ax = fig.subplots()
plt.subplots_adjust(bottom=0.5)
p, = ax.plot(x_points, x_vals)
plt.ylim(0, 1)

k_slide = plt.axes((0.25, 0.1, 0.65, 0.1))
k_slider = Slider(k_slide, 'k', valmin=0, valmax=4, valinit=0, valstep=0.1)
x_slide = plt.axes((0.25, 0.2, 0.65, 0.1))
x_slider = Slider(x_slide, 'x', valmin=0, valmax=1, valinit=0, valstep=0.1)


def update_k(val):
    global k
    x_vals = values(x, val)
    p.set_ydata(x_vals)
    fig.canvas.draw()
    k = val


def update_x(val):
    global x
    x_vals = values(val, k)
    p.set_ydata(x_vals)
    fig.canvas.draw()
    x = val


x_slider.on_changed(update_x)

k_slider.on_changed(update_k)


plt.show()
