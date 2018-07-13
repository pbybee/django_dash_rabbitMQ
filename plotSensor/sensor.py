import time
import numpy as np
import random
from threading import Thread

class Sensor():

    def __init__(self, stepSize):
        self.xVals = np.zeros(100)
        self.yVals = np.zeros(100)

        self.nominal = 5
        self.stepSize = stepSize
        self.maxVal = 10
        self.minVal = 0

    def calcValue(self):
        value = self.yVals[-1]
        if value < self.nominal:
            maxStep = self.stepSize
            minStep = -1 * self.stepSize * (value - self.minVal) / (self.nominal - self.minVal)
        else:
            maxStep = self.stepSize * (self.maxVal - value) / (self.maxVal - self.nominal)
            minStep = -1 * self.stepSize
        value += random.random() * (maxStep - minStep) + minStep

        return value

    def updateSensor(self):
        self.xVals[:-1] = self.xVals[1:]
        self.xVals[-1] = self.xVals[-2] + 1

        newVal = self.calcValue()
        self.yVals[:-1] = self.yVals[1:]
        self.yVals[-1] = newVal

    def getSensorValues(self):
        self.updateSensor()
        return {'x': self.xVals, 'y': self.yVals}

    def startSensor(self):

        def doUpdate():
            while True:
                self.updateSensor()
                time.sleep(1000)
        p = Thread(target=doUpdate)
        p.start()
