import tkinter as tk
import numpy as np
from wave_class import Wave
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# Open tkinter class.
root=tk.Tk()

# Main window features.
root.title("Wave Generator")
root.config(bg="black")

# Create Frame
frame = tk.Frame(root, width=650, height=350, bg='red')
frame.pack()

# Wave generator.
tk.Label(frame, text='Wave Generator.').place(x=100, y=200)

# tk.Label(root, text="Frequency [Hz]").grid(row=0)
# tk.Label(root, text="Time [secs]").grid(row=1)
# freq = tk.Entry(root)
# time = tk.Entry(root)

# # Grid placing.
# freq.grid(row=0, column=1)
# time.grid(row=1, column=1)

# wave_type = 'sawtooth'
# wave = Wave(freq, time, wave_type)

# # Creates Figure.
# fig = Figure(figsize=(5, 4), dpi=100)
# fig.add_subplot(111).plot(wave.timevector, wave.wave)

# # A tk.DrawingArea.
# canvas = FigureCanvasTkAgg(fig, master=root)  
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # Matplotlib Toolbar
# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Closing the loop.
root.mainloop() 