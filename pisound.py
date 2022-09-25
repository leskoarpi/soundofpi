import pyaudio
import numpy as np


p = pyaudio.PyAudio()

volume = 0.8     # range [0.0, 1.0]
fs = 7000      # sampling rate, Hz, must be integer
duration = 0.4   # in seconds, may be float
#f = 50       # sine frequency, Hz, may be float

hanglista = [415.413, 440.0, 493.858, 523.225, 587.275, 659.187, 698.376, 830.491, 880.0, 987.069] #Hz
with open('pi.txt') as fajl:
    for line in fajl:
        for szam in line:
    
            #print(szam)
            # generate samples, note conversion to float32 array
            samples = (np.sin(2*np.pi*np.arange(fs*duration)*(hanglista[int(szam)]/2)/fs)).astype(np.float32).tobytes()


            # for paFloat32 sample values must be in range [-1.0, 1.0]
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=fs,
                            output=True)

            # play. May repeat with different volume values (if done interactively) 
            stream.write(samples)

            stream.stop_stream()
            stream.close()

p.terminate()
