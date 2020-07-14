import serial 
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

from tkinter import Tk, END, LabelFrame, Text, Label, Frame, Button, LEFT
from sklearn.preprocessing import StandardScaler
from numpy import abs as np_abs
from numpy.fft import rfft

sc = StandardScaler()
SpeedCon = 9600
lenInData = 1024 # len input data from COM port and other
facecolor = '#D0ECE6'

def SerialReadAndWrite(): # write signal from sensor in file .csv
    ser = serial.Serial('', SpeedCon,timeout=1) #in '' need write com port
    serArrData += ser.read(lenInData)
    with open('SensorData.csv', 'w+') as f:
        w = csv.writer(f)

#def GetFFTFromInpuyDat(): # get FFT from file .csv 
    #for i in range(0, len(serArrData)):
    #    spectrum = rfft(serArrData[i], lenInData) # get FFT from input data
    #    spectrumABC = np_abs(spectrum) # get abc from FFT 
    #    spectrumArr += spectrumABC # array fo spectrogramma

def OutputFFT():
    fig, alex = plt.subplots(figsize = (9, 4), facecolor = facecolor)
    plt.xlabel('Time, s', frontsize = 'xx-large')
    plt.ylabel('Frequency, Hz', frontsize = 'xx-large')
    cmap = plt.get_cmap('magma')
    
root = Tk()
root.title("")

f_top = LabelFrame (root)

ButtonZone = Frame()
ButtonZone.pack()

buttonRead = Button(ButtonZone, text = "Read", command = SerialReadAndWrite)
buttonRead.pack(side = LEFT)

buttonFFT = Button(ButtonZone, text = "FFT", command = SerialReadAndWrite)
buttonFFT.pack(side = LEFT)

buttonOutput = Button(ButtonZone, text = "Output", command = SerialReadAndWrite)
buttonOutput.pack(side = LEFT)

root.mainloop()
