import tkinter as tk
import numpy as np
from wave_class import Wave
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Application(tk.Frame):
    pass

# Open tkinter class.
root=tk.Tk()

# Root config.
root.title("Wave Generator")
root.config(bg="white")

# Creating Frames
graph_frame = tk.Frame(root, width=1200, height=600)
graph_frame.pack(fill='both', expand='True')
graph_frame.config(bd=35)

# Functions.
    
def plotting():
    pass

def submit():
    freq = float(entryFreq.get())
    time = float(entryTime.get())
    wave_type = 'sawtooth'
    wave = Wave(freq, time, wave_type)
    # fig.add_subplot(111).plot(wave.timevector, wave.wave)
    plt.plot(wave.timevector, wave.wave)

# Creating Labels and Entries.
labelTitle = tk.Label(graph_frame, text='Insert Data.')
labelFreq = tk.Label(graph_frame, text='Frequency [Hz]')
labelTime = tk.Label(graph_frame, text='Time [secs]')
freq = tk.IntVar()
time = tk.IntVar()
entryFreq = tk.Entry(graph_frame)
entryTime = tk.Entry(graph_frame)
submitButton = tk.Button(graph_frame, text='Submit', command=submit)
   
    
# Grid placing.
labelTitle.grid(row=0)
labelFreq.grid(row=1, column=0, sticky='e', padx=5, pady=5)
labelTime.grid(row=2, column=0, sticky='e', padx=5, pady=5)
entryFreq.grid(row=1, column=1)
entryTime.grid(row=2, column=1)
submitButton.grid(row=3, column=1)

# Creates Figure.
fig = Figure(figsize=(5, 4), dpi=100)
time_vector = np.linspace(0,1,44100)
wave = np.sin(2*np.pi*time_vector)
fig.add_subplot(111).plot(time_vector, wave)

# A tk.DrawingArea.
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Matplotlib Toolbar
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Closing the loop.
root.mainloop() 