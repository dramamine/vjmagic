import serial

import serial.tools.list_ports
print([comport.device for comport in serial.tools.list_ports.comports()])

# ser = serial.Serial('COM3')  # open serial port
# print(ser.name)         # check which port was really used
# ser.write(b'hello')     # write a string
# ser.close()             # close port

ser = serial.Serial('COM3', 9600, timeout=1)

def sense_things(cb):
    while True:
        line = ser.readline().rstrip()
        value = [int(word) for word in line.split() if word.isdigit()]
        if value:
            cb(value[0])
        # print(type(line))
