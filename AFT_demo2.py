# https://www.youtube.com/watch?v=spUNpyF58BY
# But what is the Fourier Transform? A visual introduction.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Slider

t = np.linspace(0, 5, 1000)
w = np.linspace(0, 5, 1000)

init_freq = 3
winding_freq = init_freq


def f(times, amp, freq):
    return amp * np.sin(2*np.pi*freq*times + np.pi/2)


def g(times, amp, freq, w_freq):
    r = f(times, amp, freq)
    theta = -w_freq * 2 * np.pi * times
    x = r * np.cos(theta)
    return np.sum(x) / len(x)


def h(times, amp, freq, w_freqs):
    ws = []
    for i in w_freqs:
        ws += [g(times, amp, freq, i)]
    return ws

"""
def g(times, amp, freq, w_freq):
    xs = []
    for i in times:
        r = f(i, amp, freq)
        theta = -w_freq * 2 * np.pi * i
        x = r * np.cos(theta)
        xs += [x]

    return np.sum(xs) / len(xs)
"""


print(g(t, 5, init_freq, winding_freq))

fig, ax_carthesian = plt.subplots()
line, = ax_carthesian.plot(t, f(t, 5, init_freq), lw=2)

fig.subplots_adjust(bottom=0.75)

ax_polar = fig.add_axes([-0.25, 0.25, 1, 0.4], polar=True)
ax_polar.set_rmax(5)
line2, = ax_polar.plot(-winding_freq*2*np.pi*t, f(t, 5, init_freq), lw=2)

ax_winding = fig.add_axes([0.5, 0.25, 0.4, 0.4])
line3, = ax_winding.plot(w, h(t, 5, init_freq, w), lw=2)

ax_freq = fig.add_axes([0.25, 0.05, 0.65, 0.03])
freq_slider = Slider(
    ax=ax_freq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=10,
    valinit=init_freq
)


def update_freq(val):
    line.set_ydata(f(t, 5, freq_slider.val))
    line2.set_ydata(f(t, 5, freq_slider.val))
    line2.set_xdata(-freq_slider.val * 2 * np.pi * t)
    line3.set_ydata(h(t, 5, freq_slider.val, w))


freq_slider.on_changed(update_freq)

plt.show()
