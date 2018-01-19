import spidev
import max6675
from time import sleep
while True:
    sensor_0_0 = max6675.MAX6675(24, 23, 22)
    print (sensor_0_0.get())
    sleep(0.5)


def sen(datapin):
    sensor_0_0 = max6675.MAX6675(24,23,datapin)
    return sensor_0_0.get()
