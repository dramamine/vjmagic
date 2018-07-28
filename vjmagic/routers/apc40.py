# from push.listener import PushEventListener
# from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.state import hardware
from vjmagic.state import apc40
from vjmagic.config.apc40 import config

rezzie = None
midiinput = None
midithru = None

clips_bank = 0

# constructor
def init():
    global midiinput, midithru
    # setup inputs
    midiinput = rtmidi.MidiIn()
    port = Router.find_port_index(midiinput, "apc40")
    midiinput.open_port(port)
    midiinput.set_callback(handler)
    midithru = rtmidi.MidiOut()
    portid = Router.find_port_index(midithru, "apc40")
    if portid >= 0:
      midithru.open_port(portid) 
      print("found out port for apc40.")
    else:
      print("couldnt find apc40 output, how will my lights work??")

    # init_lights()
    recolor_clips_bank(0)
    recolor_clips_leds()

def use(res):
    global rezzie
    rezzie = res

def thru(evt):
    print("thru called.", flush=True)
    evt = event[0]
    (status, data1, data2) = evt
    rezzie.thru(evt)

# this handler's probably in every router
def handler(event, data=None):

    evt = event[0]
    (status, data1, data2) = evt
    print("apc40", evt)

    check_for_bank_change(status, data1, data2)


    # forward everything to resolume
    rezzie.thru(evt)

def check_for_bank_change(status, data1, data2):
    global clips_bank
    clips_banks = config['clips_banks']
    idx = 0
    for bank in clips_banks:
        if status == bank[0] and data1 == bank[1]:
            clips_bank = idx
            print('ok! updating clip bank to:', idx)
            recolor_clips_bank(idx)
            recolor_clips_leds()
            return 
        idx += 1

def recolor_clips_bank(current_bank):
    print("recoloring bank..", current_bank)
    clips_banks = config['clips_banks']
    clips_banks_off = config['clips_banks_off']

    idx = 0
    for message in clips_banks:
        if idx == current_bank:
            midithru.send_message(message)
        else:
            midithru.send_message(clips_banks_off[idx])
        idx += 1

def recolor_clips_leds():
    global clips_bank
    clips_leds = config['clips_leds']
    clips_colors = config['clips_colors']
    clip_color = clips_colors[clips_bank]
    for led in clips_leds:
         midithru.send_message([apc40.NOTE_ON_CH1, led, clip_color])
         clip_color = clip_color + 1



def init_lights():
    # this works fine for turning those 4 buttons on.
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.RECORD_BUTTON, 1])
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.SOLO_BUTTON, 1])
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.TRACK_SELECT, 1])
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.CROSSFADER, 2])

    midithru.send_message([apc40.NOTE_ON_CH1, 0, 81])
    midithru.send_message([apc40.NOTE_ON_CH1, 8, 82])
    midithru.send_message([apc40.NOTE_ON_CH1, 16, 83])
    midithru.send_message([apc40.NOTE_ON_CH1, 24, 84])

    return

