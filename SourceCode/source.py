import serial 
import pandas as pd
import numpy as np
import csv
import mathotlib.pyplot as plt

from numpy import abs as np_abs
from numpy.fft import rfft

sc = StandardScaler()
SpeedCon = 9600
lenInData = 1024 # lenght input data from COM port and other
facecolor = '#D0ECE6'

def SerialReadAndWrite(): # write signal from sensor in file .csv
    ser = serial.Serial('', SpeedCon,timeout=1) #in '' need write com port
    serArrData += ser.read(lenInData)
    with open('SensorData.csv', 'w+') as f:


def GetFFTFromInpuyDat(): # get FFT from file .csv 
    #for i in range(0, len(serArrData)):
    #    spectrum = rfft(serArrData[i], lenInData) # get FFT from input data
    #    spectrumABC = np_abs(spectrum) 
    #    spectrumArr += spectrumABC 

def OutputFFT():
    fig, alex = plt.subplots(figsize = (9, 4), facecolor = facecolor)
    plt.xlabel('Time, s', frontsize = 'xx-large')
    plt.ylabel('Frequency, Hz', frontsize = 'xx-large')
    cmap = plt.get_cmap('magma')
    
