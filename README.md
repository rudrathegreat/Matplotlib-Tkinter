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

> You can create a line plot with text labels using `Python plot().`
>
> Multiple axes (i.e. subplots) are created with the`Python subplot()` function
>
> Matplotlib can display images (assuming equally spaced horizontal dimensions) using the `Python imshow()` function
>
> The `Python pcolormesh()` function can make a colored representation of a two-dimensional array, even if the horizontal dimensions are unevenly spaced. The `Python contour()` function is another way to represent the same data
>
> The`Python hist()` function automatically generates histograms and returns the bin counts or probabilities
>
> You can add arbitrary paths in Matplotlib using the `Python matplotlib.path` module
>
> The mplot3d toolkit (see Getting started and 3D plotting) has support for simple 3d graphs including surface, wireframe, scatter, and bar charts.
>
> etc.

## More Complicated Stuff...

`Python matplotlib.pyplot` is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In `Python matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that “axes” here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).

Generating visualizations with pyplot is very quick:

```Python

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

```

to...

There are some instances where you have data in a format that lets you access particular variables with strings. For example, with `Python numpy.recarray` or `Python pandas.DataFrame`.

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

To make a window, call Tkinter and then use `Python Tk()` to make a window, then add `Python Tk.mainloop()` to keep the window up and running.

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
button = Button
