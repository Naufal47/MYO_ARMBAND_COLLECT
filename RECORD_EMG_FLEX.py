import serial
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
import myo
from threading import Lock, Thread
from scipy.interpolate import interp1d

# --------------------------------------------------------------------------------------
# PROGRAM PENGAMBIAN DATA KEKUATAN
# --------------------------------------------------------------------------------------
ser = serial.Serial('com7',baudrate=2000000)
data = []
start_time = time.time()
data_final=[]
seconds = 90
collectt=True
balanced_data_target = 18000

def interpolate_column(column):
    interpolasi = interp1d(np.linspace(0, 1, len(column)), column)
    return interpolasi(np.linspace(0, 1, balanced_data_target))

def flex():
    global collectt
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time-start_time
        arduino_data = ser.readline().decode('ascii', errors = 'ignore')
        arduino_data = arduino_data.strip().split(" ")
        # data.append(arduino_data)
        
        if elapsed_time >= 1:
            break
    time.sleep(3)
    start_time = time.time()
    print('=========Mulai==========')
    while collectt:
        current_time = time.time()
        elapsed_time = current_time-start_time
        
        arduino_data = ser.readline().decode('ascii', errors = 'ignore')
        arduino_data = arduino_data.strip().split(" ")
        data.append(arduino_data)
        t = int(elapsed_time)
        print(t, end='\r')
        if t==0 or t==15 or t==30 or t==45 or t==60 or t==75:
            print('      =======> GENGGAM <========', end='\r' )
        elif t==5 or t==20 or t==35 or t==50 or t==65 or t==80:
            print('      =========>LEPASKAN<=======', end='\r')
        elif t==10 or t==25 or t==40 or t==55 or t==70 or t==85:
            print('      =========>ISTIRAHAT<======', end='\r')

        if elapsed_time >= seconds:
            collectt=False
            break
    data2=pd.DataFrame(data)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # data2.to_csv('barusudut_naufal1.csv', index=False)
    dataflex = pd.DataFrame(np.array(data2[0].str.split(',',expand=True)))
    data1_interpolated = dataflex.apply(interpolate_column)
    data1_interpolated.to_csv('sudut_grip_naufal4.csv', index=False)
     #<------------NAMA FILE FLEX----------
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    print(len(data2))
    print("========While Loop Berhenti=========")

# -----------------------------------------------------------------------------------
# PROGRAM PENGAMBILAN DATA EMG (MYO ARMBAND)
# -----------------------------------------------------------------------------------
class EmgCollector(myo.DeviceListener):
    """
    Collects EMG data in a queue with *n* maximum number of elements.
    """

    def __init__(self, n):
        self.n = n
        self.lock = Lock()
        self.emg_data_queue = deque(maxlen=n)

    def get_emg_data(self):
        with self.lock:
            return list(self.emg_data_queue)

    # myo.DeviceListener

    def on_connected(self, event):
        event.device.stream_emg(True)

    def on_emg(self, event):
        with self.lock:
            self.emg_data_queue.append((event.timestamp, event.emg))

class Plot(object):
    def __init__(self, listener):
        self.n = listener.n
        self.listener = listener
        self.start_time=time.time()
        self.curent_time=time.time()
        self.elapsetime=self.curent_time-self.start_time
        self.collect=True
        self.seconds=50
        self.fig = plt.figure()
        self.axes = [self.fig.add_subplot('81' + str(i)) for i in range(1, 9)]
        [(ax.set_ylim([-100, 100])) for ax in self.axes]
        self.graphs = [ax.plot(np.arange(self.n), np.zeros(self.n))[0] for ax in self.axes]
        plt.ion()

    def update_plot(self):
        emg_data = self.listener.get_emg_data()
        emg_data = np.array([x[1] for x in emg_data]).T
        save_emg = pd.DataFrame(emg_data)
        save_emgTranspose = save_emg.T
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        save_emgTranspose.to_csv('myo_naufal4.csv',index=False) #<--------NAMA FILE EMG----
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        for g, data in zip(self.graphs, emg_data):
            if len(data) < self.n:
                # Fill the left side with zeroes.
                data = np.concatenate([np.zeros(self.n - len(data)), data])
            g.set_ydata(data)

        plt.draw()
    def main(self):
        global collectt
        while collectt:
            self.update_plot()
            plt.pause(1.0 / 30)
def main():
    myo.init()
    hub = myo.Hub()
    listener = EmgCollector(18000)
    with hub.run_in_background(listener.on_event):
        Plot(listener).main()
# -------------------------------------------------------------------------------------
# RUN PROGRAM PENGAMBILAN DATA EMG DAN KEKUTAN UNTUK REGRESI
# -------------------------------------------------------------------------------------

def get_data():
    p1 =Thread(target=flex)
    p2 =Thread(target=main)

    p1.start()
    p2.start() 
    # p1.join()
    # p2.join() 

if __name__=='__main__':
    get_data()
        
