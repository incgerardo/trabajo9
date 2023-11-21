import numpy as np
from scipy.io import wavfile

# Cargar el archivo WAV
archivo_wav = "audio.wav"
frecuencia_muestreo, datos = wavfile.read(archivo_wav)

print(frecuencia_muestreo)

# Calcular la Transformada de Fourier
transformada_fourier = np.fft.fft(datos)

# Calcular las amplitudes de las frecuencias
amplitudes = np.abs(transformada_fourier)
frecuencias = np.fft.fftfreq(len(amplitudes), 1 / frecuencia_muestreo)

print(type(amplitudes))

print("Todas las frecuencias encontradas con sus amplitudes:")
#for i, (frecuencia, amplitud) in enumerate(zip(frecuencias, amplitudes), 1):
#    print(f"{i}. Frecuencia: {abs(frecuencia):.2f} Hz - Amplitud: {abs(amplitud)}")
