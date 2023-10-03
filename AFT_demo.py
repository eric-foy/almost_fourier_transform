# https://www.youtube.com/watch?v=spUNpyF58BY
# But what is the Fourier Transform? A visual introduction.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Slider


def f(t, amp, freq):
    return amp * np.sin(2*np.pi*freq*t + np.pi/2)


t = np.linspace(0, 5, 1000)

init_freq = 3
winding_freq = 0.5

fig, ax_carthesian = plt.subplots()
line, = ax_carthesian.plot(t, f(t, 5, init_freq), lw=2)

fig.subplots_adjust(bottom=0.75)

ax_polar = fig.add_axes([0, 0.25, 1, 0.4], polar=True)
ax_polar.set_rmax(5)
line2, = ax_polar.plot(winding_freq*2*np.pi*t, f(t, 5, init_freq), lw=2)

ax_freq = fig.add_axes([0.25, 0.05, 0.65, 0.03])
freq_slider = Slider(
    ax=ax_freq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=10,
    valinit=init_freq
)

ax_winding = fig.add_axes([0.25, 0.15, 0.65, 0.03])
winding_slider = Slider(
    ax=ax_winding,
    label='Winding [Hz]',
    valmin=0.1,
    valmax=10,
    valinit=winding_freq
)


def update_freq(val):
    line.set_ydata(f(t, 5, freq_slider.val))
    line2.set_ydata(f(t, 5, freq_slider.val))


def update_winding(val):
    line2.set_xdata(winding_slider.val * 2 * np.pi * t)
    fig.canvas.draw_idle()


freq_slider.on_changed(update_freq)
winding_slider.on_changed(update_winding)

plt.show()
