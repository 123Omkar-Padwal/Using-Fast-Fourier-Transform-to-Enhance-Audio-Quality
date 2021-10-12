from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

def main(fs,audio):
    
    duration  = len(audio)/fs
    time = np.linspace(0,duration,len(audio))
    return time

def plot_time_spectrum(audio,time):
    plt.plot(time,audio)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Time vs Amplitude')
    plt.show()
    
def plot_frequency_spectrum(fs,audio):
    yfft = np.fft.fft(audio)
    xfft = np.linspace(0,fs,len(yfft))
    plt.plot(xfft[:len(xfft)//2], abs(yfft[:len(yfft)//2]))
    plt.title('Linear FFT')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()
    plt.plot(np.log10(xfft[:len(xfft)//2]), 20*np.log10(abs(yfft[:len(yfft)//2])))
    plt.title('Logarithmic FFT')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude(db)')
    
def voice_enhancer(fs,audio):
    yfft = np.fft.fft(audio)
    xfft = np.linspace(0,fs,len(yfft))
    for lower_bound, upper_bound, enhancer in ((120,180,10),(0,0,0)):
        y_index1 = int(np.round((len(audio)/fs)*lower_bound))
        y_index2 = int(np.round((len(audio)/fs)*upper_bound))
        yfft[y_index1:y_index2+1]*=enhancer
    plt.plot(xfft[:len(xfft)//2], abs(yfft[:len(yfft)//2]))
    plt.title('Enhanced Linear FFT')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()
    inv_yfft=np.fft.ifft(yfft)
    inv_yfft=np.real(inv_yfft).astype(np.int16)
    return inv_yfft
    
    pass    
if __name__=='__main__':
    fs, audio = wavfile.read('Omkar_dspaudio2.wav')
    time=main(fs,audio)
    plot_time_spectrum(audio,time)
    plot_frequency_spectrum(fs,audio)
    inv_fft=voice_enhancer(fs,audio)
    wavfile.write('enhanced.wav', fs, inv_fft)