import time
import rtmidi
import itertools
from random import shuffle
# from apscheduler.schedulers.background import BackgroundScheduler
# scheduler = BackgroundScheduler()
device_id = "PXT out 8"

midiin = rtmidi.MidiIn()



def handle_midi_input(event, data=None):
  print event
  # message, note, vel = event[0]
  # if message == 0x90:
  #   print "yep this is a note on message"
  # print note


available_ports = midiin.get_ports()
try:
    push = available_ports.index(device_id)
except ValueError:
    print "no device with the hardcoded id", device_id
    print "available devices are:"
    for idx, val in enumerate(available_ports):
        print idx, ': ', val
    quit()

if push >= 0:
    midiin.open_port(push)
    midiin.set_callback(handle_midi_input)

while(True):
    time.sleep(5)
