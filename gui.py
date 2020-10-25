import tkinter as tk
import numpy as np
from wave_class import Wave
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Wave Generator")
        self.root.config(bg="white")
        self.root.geometry('800x600')
        
        tk.Label(self.root, text='Wave Generator').pack(side="top")
        
        self.inputFrame = self.InputFrame(self.root)
        self.plottingFrame = self.PlottingFrame(self.root)
        
        self.inputFrame.plotButton=tk.Button(self.inputFrame.inputFrame, text="Plot", command=lambda: self.submit())
        self.inputFrame.plotButton.grid(row=3,column=1)        

    def submit(self):
        self.inputFrame.submit()        
        self.plottingFrame.plot(self.inputFrame.wave.time_vector, self.inputFrame.wave.wave)

    class InputFrame:
        def __init__(self, root):
            self.root = root
            self.inputFrame = tk.Frame(self.root, width=800, height=600)
            self.inputFrame.pack(fill='both', expand='True')
            self.inputFrame.config(bd=35)
            
            tk.Label(self.inputFrame, text='Insert Data.').grid(row=0)
            tk.Label(self.inputFrame, text='Frequency [Hz]').grid(row=1, column=0, sticky='e', padx=5, pady=5)
            tk.Label(self.inputFrame, text='Time [secs]').grid(row=2, column=0, sticky='e', padx=5, pady=5)
            self.playButton = tk.Button(self.inputFrame, text='Play', command=lambda: self.play())
            
            self.freq = tk.IntVar()
            self.time = tk.IntVar()
            self.entryFreq = tk.Entry(self.inputFrame)
            self.entryTime = tk.Entry(self.inputFrame)
            self.entryFreq.grid(row=1, column=1)
            self.entryTime.grid(row=2, column=1)    
            self.playButton.grid(row=3, column=0)

        def submit(self):
            self.freq = float(self.entryFreq.get())
            self.time = float(self.entryTime.get())
            self.wave_type = 'sine'
            self.wave = Wave(self.freq, self.time, self.wave_type)
            
        def play(self):
            self.submit()
            self.wave.play()
        
    class PlottingFrame:
        
        def __init__(self, root):
            self.root=root
            # Creates Figure.
            time_vector = np.linspace(0,1,44100)
            wave = np.sin(2*np.pi*time_vector)
            fig = plt.figure(figsize=(8,8))
            self.ax = fig.add_subplot(1,1,1)
            self.ax.plot(time_vector, wave)
          
            # A tk.DrawingArea.
            self.canvas = FigureCanvasTkAgg(fig, master=self.root)  
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
            # Matplotlib Toolbar
            toolbar = NavigationToolbar2Tk(self.canvas, root)
            toolbar.update()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def plot(self, time_vector, wave):
            self.ax.clear()
            self.ax.plot(time_vector,wave,color='red')
            self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    Application(root)
    root.mainloop()


# def submit():
#     freq = float(entryFreq.get())
#     time = float(entryTime.get())
#     wave_type = 'sawtooth'
#     wave = Wave(freq, time, wave_type)
#     # fig.add_subplot(111).plot(wave.timevector, wave.wave)
#     plt.plot(wave.timevector, wave.wave)

# # Creating Labels and Entries.
# labelTitle = tk.Label(graph_frame, text='Insert Data.')
# labelFreq = tk.Label(graph_frame, text='Frequency [Hz]')
# labelTime = tk.Label(graph_frame, text='Time [secs]')
# freq = tk.IntVar()
# time = tk.IntVar()
# entryFreq = tk.Entry(graph_frame)
# entryTime = tk.Entry(graph_frame)
# submitButton = tk.Button(graph_frame, text='Submit', command=submit)
   
    
# # Grid placing.
# labelTitle.grid(row=0)
# labelFreq.grid(row=1, column=0, sticky='e', padx=5, pady=5)
# labelTime.grid(row=2, column=0, sticky='e', padx=5, pady=5)
# entryFreq.grid(row=1, column=1)
# entryTime.grid(row=2, column=1)
# submitButton.grid(row=3, column=1)

# # Creates Figure.
# fig = Figure(figsize=(5, 4), dpi=100)
# time_vector = np.linspace(0,1,44100)
# wave = np.sin(2*np.pi*time_vector)
# fig.add_subplot(111).plot(time_vector, wave)

# # A tk.DrawingArea.
# canvas = FigureCanvasTkAgg(fig, master=root)  
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # Matplotlib Toolbar
# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
