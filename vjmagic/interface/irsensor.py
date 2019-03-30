import aioserial
import asyncio

# find port name
# import serial.tools.list_ports
# print([comport.device for comport in serial.tools.list_ports.comports()])

# callback for values
listener = None

# if True, call the callback/listener when getting values
ears = False
last_values = [99, 100, 101, 102, 103]

async def get_values(aioserial_instance: aioserial.AioSerial):
    global last_values
    while True:
        text = (await aioserial_instance.readline_async()).decode(errors='ignore')
        if ears:
            try:
                val = int(text)
            except:
                val = 0
            # print('my val:', val)
            if val > 0:
                last_values.append(val)
                last_values = last_values[1:]

                sorted_values = sorted(last_values)
                if listener:
                    listener(sorted_values[2])


# are we listening for this stuff, or not?
def toggle_ears(boole):
    global ears
    ears = boole

# attach listener to the serial data
def sense_things(cb):
    global listener
    listener = cb
    run()

def run():
    asyncio.run(get_values(aioserial.AioSerial(port='COM3')))
