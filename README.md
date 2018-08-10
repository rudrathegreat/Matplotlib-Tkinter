# Using Matplotlib in Tkinter
## Overview

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

## Installing Matplotlib

Matplotlib and most of its dependencies are all available as wheel packages for macOS, Windows and Linux distributions:

```Bash

python -mpip install -U pip
python -mpip install -U matplotlib

```

If you are using Python 2.7 on a Mac you may need to do:

```Bash

xcode-select --install

```

## Getting Started

> You can create a line plot with text labels using `plot()`
>
> Multiple axes (i.e. subplots) are created with the`subplot()` function
>
> Matplotlib can display images (assuming equally spaced horizontal dimensions) using the `imshow()` function
>
> The `pcolormesh()` function can make a colored representation of a two-dimensional array, even if the horizontal dimensions are unevenly spaced. The `contour()` function is another way to represent the same data
>
> The`hist()` function automatically generates histograms and returns the bin counts or probabilities
>
> You can add arbitrary paths in Matplotlib using the `matplotlib.path` module
>
> The mplot3d toolkit (see Getting started and 3D plotting) has support for simple 3d graphs including surface, wireframe, scatter, and bar charts.
>
> etc.

## More Complicated Stuff...

`matplotlib.pyplot` is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that “axes” here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).

Generating visualizations with pyplot is very quick:

```Python

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

```

to...

There are some instances where you have data in a format that lets you access particular variables with strings. For example, with `numpy.recarray` or `pandas.DataFrame`.

Matplotlib allows you provide such an object with the data keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.

```Python

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

```

## Intro to Tkinter
### Make a Window

To make a window, call Tkinter and then use `Tk()` to make a window, then add `Tk.mainloop()` to keep the window up and running.

```Python

from tkinter import *

root = Tk()
root.mainloop()

```

### Text Box

Using root, we can make a text box. We just have to tell the text box which window to be in -

```Python

from tkinter import *

root = Tk()
Box = Text(root, width = 300, height = 500)
Box.pack()

root.mainloop()

```

### Make a Button

To make a button, simply - 

```Python

from tkinter import *

root = Tk()
button = Button(root, text = 'Quit', command = master.quit)
button.pack()

root.mainloop()

```

## Os

Os is used to save files. To save some text into a file, simply -

```Python

import os.path

text = 'Hi my name is John!'
path = 'D:\John\Documnts\file.txt'

file_handle = open(path, 'a') # a means to append. w means to overwrite
file_handle.write(text)
file_handle.close()

```

## Embedding in a Tk Canvas

To put it simple, you use a backend called `TkAgg` which allows you Matplotlib to be displayed in Tkinter. You can then add styles and uniqueness using `plt.style.use('style')`. Simply -

```Python

import matplotlib as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo

# Create a canvas
w, h = 300, 200
window = tk.Tk()
window.title("A figure in a canvas")
canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()

# Generate some example data
X = np.linspace(0, 2 * np.pi, 50)
Y = np.sin(X)

# Create the figure we desire to add to an existing canvas
fig = mpl.figure.Figure(figsize=(2, 1))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig_x, fig_y = 100, 100
fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()

# Add more elements to the canvas, potentially on top of the figure
canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
canvas.create_text(200, 50, text="Zero-crossing", anchor="s")

# Let Tk take over
tk.mainloop()

```

It will show a sin-wave type graph.

## Why Use It?

We are using these two modules to make a GUI Interface which will give us information about water quality in a nearby river. It will show temperature, pH and conductivity and lively update and save documents.

We will also be using LoRa to transmit the data over long distances.

Here is a quick overview of the project - 

The aim of this project is to install smart water sensors into local areas known to be habitats for platypus. The will utilise environmental sensors connected to BBC Microbit which will allow the sensors to withdraw and store water quality information which is displayed nearby at signed stations. The signed stations will display the relevant information and act as a point where emergency information can be sent via 4G networks to relevant authorities. The equipment is to be designed utilising small-scale electronics powered by solar panels, as well as the BBC Microbit and E-waste which will allow for local students and community engagement. This allows the project to act as an educational tool that can raise awareness of Stormwater pollution.
All explanations are commented in code.

Here is a quick peep of the code -

**NOTE** - THIS IS NOT THE ENTIRE CODE

```Python

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
#import serial
from random import randint
import os.path
from datetime import *
from time import sleep
import matplotlib.dates as mdates

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
```

## Further Links

You check out these links to go to further links -

> https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_canvas_sgskip.html
>
> https://matplotlib.org/tutorials/introductory/customizing.html#sphx-glr-tutorials-introductory-customizing-py
>
> https://matplotlib.org/tutorials/index.html
>
> https://matplotlib.org/
>
> https://www.python-course.eu/tkinter_buttons.php
>
> https://github.com/PlatypusProject/Platypus-Monitoring-Project
>
> https://github.com/rudrathegreat
>
> https://www.python.org
