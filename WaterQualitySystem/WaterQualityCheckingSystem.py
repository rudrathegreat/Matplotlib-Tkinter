from _pydecimal import Decimal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import tkinter as tk
from tkinter import ttk
from datetime import *
import matplotlib
from matplotlib import style

matplotlib.use("TkAgg")

LARGE_FONT = ("Verdana", 16)
MEDIUM_FONT = ("Verdana", 12)
style.use("ggplot")
DataFilePathTemperature = "files/temperature.txt"
DataFilePathConductivity = "files/conductivity.txt"
DataFilePathpH = "files/pH.txt"

# Figures and plots for Temperature
last24HoursFigureTemperature = Figure(figsize=(5, 5), dpi=100)
pltLast24HoursTemperature = last24HoursFigureTemperature.add_subplot(111)
lastYearFigureTemperature = Figure(figsize=(5, 5), dpi=100)
pltLastYearTemperature = lastYearFigureTemperature.add_subplot(111)

# Figures and plots for Conductivity
last24HoursFigureConductivity = Figure(figsize=(5, 5), dpi=100)
pltLast24HoursConductivity = last24HoursFigureConductivity.add_subplot(111)
lastYearFigureConductivity = Figure(figsize=(5, 5), dpi=100)
pltLastYearConductivity = lastYearFigureConductivity.add_subplot(111)

# Figures and plots for pH
last24HoursFigurePh = Figure(figsize=(5, 5), dpi=100)
pltLast24HoursPh = last24HoursFigurePh.add_subplot(111)
lastYearFigurePh = Figure(figsize=(5, 5), dpi=100)
pltLastYearPh = lastYearFigurePh.add_subplot(111)


def animateLast24HoursTemperature(i):
    pullData = open(DataFilePathTemperature, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'
    for eachLine in dataList:
        if len(eachLine) > 1:
            date, temp = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 1:
                date, time = date.split(' ')
                hour, minute, second = time.split(':')
                # xList.append(Decimal(hour))
                xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":00"
                xList.append(xAxisDateTime)
                yList.append(Decimal(temp))

                pltLast24HoursTemperature.clear()
                pltLast24HoursTemperature.set_title(str(timestamp1.date().year) + " Temperature Graph")
                pltLast24HoursTemperature.set_ylabel("Temperature (Degrees Celcius)")

                pltLast24HoursTemperature.set_xlabel("Hour Wise Data")

                pltLast24HoursTemperature.scatter(xList, yList, marker='.')
                last24HoursFigureTemperature.autofmt_xdate()


def animateLastYearTemperature(i):
    pullData = open(DataFilePathTemperature, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'

    for eachLine in dataList:
        if len(eachLine) > 1:
            date, temp = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 365:
                date, time = date.split(' ')
                xAxisDateTime = str(timestamp1.date().year) + " " \
                                + timestamp1.date().strftime('%b')
                xList.append(xAxisDateTime)
                yList.append(Decimal(temp))
                pltLastYearTemperature.clear()
                pltLastYearTemperature.set_title(str(timestamp1.date().year) + " Temperature Graph")
                pltLastYearTemperature.set_ylabel("Temperature (Degrees Celcius)")
                pltLastYearTemperature.set_xlabel("Month Wise Data ")

                pltLastYearTemperature.scatter(xList, yList, marker='.')
                lastYearFigureTemperature.autofmt_xdate()


def animateLast24HoursConductivity(i):
    pullData = open(DataFilePathConductivity, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'
    for eachLine in dataList:
        if len(eachLine) > 1:
            date, cond = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 1:
                date, time = date.split(' ')
                hour, minute, second = time.split(':')
                xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":00"
                xList.append(xAxisDateTime)
                yList.append(Decimal(cond))

                pltLast24HoursConductivity.clear()
                pltLast24HoursConductivity.set_title(str(timestamp1.date().year) + " Conductivity Graph")
                pltLast24HoursConductivity.set_ylabel("Conductivity (uS/Cm)")

                pltLast24HoursConductivity.set_xlabel("Hour Wise Data ")

                pltLast24HoursConductivity.scatter(xList, yList, marker='.')
                last24HoursFigureConductivity.autofmt_xdate()


def animateLastYearConductivity(i):
    pullData = open(DataFilePathConductivity, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'

    for eachLine in dataList:
        if len(eachLine) > 1:
            date, cond = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 365:
                date, time = date.split(' ')
                xAxisDateTime = str(timestamp1.date().year) + " " \
                                + timestamp1.date().strftime('%b')
                xList.append(xAxisDateTime)
                yList.append(Decimal(cond))
                pltLastYearConductivity.clear()
                pltLastYearConductivity.set_title(str(timestamp1.date().year) + " Conductivity Graph")
                pltLastYearConductivity.set_ylabel("Conductivity (uS/Cm)")

                pltLastYearConductivity.set_xlabel("Month Wise Data ")

                pltLastYearConductivity.scatter(xList, yList, marker='.')
                lastYearFigureConductivity.autofmt_xdate()


def animateLast24HoursPh(i):
    pullData = open(DataFilePathpH, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'
    for eachLine in dataList:
        if len(eachLine) > 1:
            date, ph = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 1:
                date, time = date.split(' ')
                hour, minute, second = time.split(':')
                xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":00"
                xList.append(xAxisDateTime)
                yList.append(Decimal(ph))
                pltLast24HoursPh.clear()

                pltLast24HoursPh.set_title(str(timestamp1.date().year) + " pH Graph")
                pltLast24HoursPh.set_ylabel("pH Value")
                pltLast24HoursPh.set_xlabel("Hour Wise Data ")

                pltLast24HoursPh.scatter(xList, yList, marker='.')
                last24HoursFigurePh.autofmt_xdate()


def animateLastYearPh(i):
    pullData = open(DataFilePathpH, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'

    for eachLine in dataList:
        if len(eachLine) > 1:
            date, ph = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 365:
                date, time = date.split(' ')
                xAxisDateTime = str(timestamp1.date().year) + " " \
                                + timestamp1.date().strftime('%b')
                xList.append(xAxisDateTime)
                yList.append(Decimal(ph))
                pltLastYearPh.clear()
                pltLastYearPh.set_title(str(timestamp1.date().year) + " pH Graph")
                pltLastYearPh.set_ylabel("pH Value")

                pltLastYearPh.set_xlabel("Month Wise Data ")

                pltLastYearPh.scatter(xList, yList, marker='.')
                lastYearFigurePh.autofmt_xdate()


class DataApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Water Quality Checking System")
        # receiveAndUpdateDataInFile()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=1)
        temperatureMenu = tk.Menu(menubar, tearoff=1)
        conductivityMenu = tk.Menu(menubar, tearoff=1)
        phMenu = tk.Menu(menubar, tearoff=1)
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Temperature Data", menu=temperatureMenu)
        temperatureMenu.add_command(label="Last 24 Hours",
                                    command=lambda: self.show_frame(HourlyGraphTemperature))
        temperatureMenu.add_separator()
        temperatureMenu.add_command(label="Last Year",
                                    command=lambda: self.show_frame(MonthlyGraphTemperature))
        menubar.add_cascade(label="Conductivity Data", menu=conductivityMenu)
        conductivityMenu.add_command(label="Last 24 Hours",
                                     command=lambda: self.show_frame(HourlyGraphConductivity))
        conductivityMenu.add_separator()
        conductivityMenu.add_command(label="Last Year",
                                     command=lambda: self.show_frame(MonthlyGraphConductivity))
        menubar.add_cascade(label="pH Data", menu=phMenu)
        phMenu.add_command(label="Last 24 Hours", command=lambda: self.show_frame(HourlyGraphPh))
        phMenu.add_separator()
        phMenu.add_command(label="Last Year", command=lambda: self.show_frame(MonthlyGraphPh))

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (
                StartPage, HourlyGraphTemperature, MonthlyGraphTemperature, HourlyGraphConductivity,
                MonthlyGraphConductivity,
                HourlyGraphPh, MonthlyGraphPh):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="WATER QUALITY CHECKING SYSTEM", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)

        label2 = tk.Label(self,
                          text="To check or monitor Temperature Or Conductivity Or pH Data,\n Please select graph option from menubar ",
                          font=MEDIUM_FONT)
        label2.pack(pady=30, padx=10)

        self.imageConductivityPh = tk.PhotoImage(file="files\ConductivityAndPh.gif")
        imageLabelConductivityPh = tk.Label(self, image=self.imageConductivityPh)
        imageLabelConductivityPh.pack(pady=0, padx=10)


class MonthlyGraphTemperature(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Last Year Temperature Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(lastYearFigureTemperature, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class HourlyGraphTemperature(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Last 24 Hours Temperature Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        canvas = FigureCanvasTkAgg(last24HoursFigureTemperature, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class MonthlyGraphConductivity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Last Year Conductivity Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(lastYearFigureConductivity, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class HourlyGraphConductivity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Last 24 Hours Conductivity Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        canvas = FigureCanvasTkAgg(last24HoursFigureConductivity, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class MonthlyGraphPh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Last Year pH Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(lastYearFigurePh, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class HourlyGraphPh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Last 24 Hours pH Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        canvas = FigureCanvasTkAgg(last24HoursFigurePh, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = DataApp()
app.geometry("1280x720")
# Animations for Temperature
ani1 = animation.FuncAnimation(last24HoursFigureTemperature, animateLast24HoursTemperature, interval=60000,
                               blit=False)
ani2 = animation.FuncAnimation(lastYearFigureTemperature, animateLastYearTemperature, interval=60000,
                               blit=False)
# Animations for Conductivity
ani3 = animation.FuncAnimation(last24HoursFigureConductivity, animateLast24HoursConductivity, interval=60000,
                               blit=False)
ani4 = animation.FuncAnimation(lastYearFigureConductivity, animateLastYearConductivity, interval=60000,
                               blit=False)
# Animations for pH
ani5 = animation.FuncAnimation(last24HoursFigurePh, animateLast24HoursPh, interval=60000, blit=False)
ani6 = animation.FuncAnimation(lastYearFigurePh, animateLastYearPh, interval=60000, blit=False)
app.mainloop()
