import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sampling_rate, audio = wavfile.read('Omkar_dspaudio2.wav')
yaxis=np.fft.fft(audio)
xaxis=np.linspace(0,sampling_rate,len(yaxis))
plt.plot(np.log(xaxis),20*np.log(np.abs(yaxis)))
plt.title('Logarithmic axis plot')
plt.xlabel('Frequency')
plt.ylabel('Amplitude(db)')
plt.show()
plt.plot(xaxis,np.abs(yaxis))
plt.title('Linear axis plot')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()


audio_inv=np.fft.ifft(yaxis)
duration=len(audio_inv)/sampling_rate
time=np.arange(0,duration,1/sampling_rate)
plt.plot(time,np.real(audio_inv))
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

'''sampling_rate1, audio1 = wavfile.read('a.wav')
yaxis1=np.fft.fft(audio1)
xaxis1=np.linspace(0,sampling_rate1,len(yaxis1))
plt.plot(np.log(xaxis1),np.log(np.abs(yaxis1)))
#plt.plot(np.log(1690),'ro-')
plt.xlabel('Frequency')
plt.ylabel('Amplitude(db)')
plt.show()'''