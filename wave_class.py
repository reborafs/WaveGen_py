import numpy as np
import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt

class Wave():
    
    def __init__(self, freq, duration, wave_type = 'empty'):
        self.fs = 44100
        self.freq = freq
        self.time = duration
        self.timevector = np.linspace(0, self.time, round(self.fs*self.time))
        self.wave = np.zeros_like(self.timevector)
        self.wave_type = wave_type
        if wave_type == 'sine':
            self.sine()
        elif wave_type == 'square':
            self.square()
        elif wave_type == 'triangle':
            self.triangle()
        elif wave_type == 'sawtooth':
            self.sawtooth()
        
    def sine(self):
        self.wave = 0.5*np.sin(2*np.pi*self.freq*self.timevector)
        self.wave_type = 'sine'
    
    def square(self):
        half_cycle = round(self.fs/(2* self.freq))
        self.wave = np.hstack((np.ones(half_cycle),(-1)*np.ones(half_cycle)))
        while len(self.wave) <= round(self.time*self.fs):
            cycle = np.hstack((np.ones(half_cycle),(-1)*np.ones(half_cycle)))
            self.wave = np.hstack((self.wave, cycle))
        self.wave = self.wave[:round(self.time*self.fs)]
            
    def triangle(self, harmonics = 10):
        series = np.zeros_like(self.timevector)
        for i in range(0, harmonics):
            n = (2*i)+1
            arg = 2 * np.pi * self.freq * n
            series += (((-1)**i)*np.sin(arg*self.timevector))/(n**2)
        self.wave = (8/(np.pi**2)) * series
        
    def sawtooth(self, harmonics = 100):
        series = np.zeros_like(self.timevector)
        for k in range(1, harmonics):
            arg = 2 * np.pi * self.freq * k
            series += (((-1)**k)*np.sin(arg*self.timevector))/k
        self.wave = (1/2) - (1/np.pi) * series
    
    def samplerate(self, fs):
        
        if  type(fs) != int:
            if type(fs) == float:
                raise TypeError('Please input an integer.')
            else:                    
                raise TypeError('Please input a valid number.')
                
        if fs < 0:
            raise ValueError('''Frequency must be a positive integer.''')
        
        elif self.freq*2 <= fs:
            self.fs = fs
            
        else: 
            raise ValueError('''Frequency value must be two times the
            samplerate due to the Nyquist Theorem.''')
            
    def play(self):
        sd.play(self.wave,self.fs)
                             
    def save(self):
        sf.write('wave.wav', self.wave, self.fs)
        
    def plot(self):
        plt.plot(self.timevector, self.wave)
        plt.xlim(0, 0.02)
        plt.ylim(-1, 1)
        
        
#------------------------------------TEST------------------------------------#

# freq = 100
# time = 2
# wave_type = 'sawtooth'
# test = Wave(freq, time, wave_type)
# plt.plot(test.timevector, test.wave)
# plt.xlim(0, 0.02)



    
