# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.state import hardware
from vjmagic.config.midifighter import config

rezzie = None
midiinput = None
midithru = None

# constructor
def init(skip = True):
    global midiinput, midithru
    # setup inputs
    midiinput = rtmidi.MidiIn()
    port = Router.find_port_index(midiinput, "midi fighter 64", skip)
    if port == -1:
      print('couldnt find an 8x8 button grid! is it plugged in??')
      exit(-1)    
    midiinput.open_port(port)
    midiinput.set_callback(handler)
    midithru = rtmidi.MidiOut()
    portid = Router.find_port_index(midithru, "midi fighter 64", skip)
    if port == -1:
      print('couldnt find the second 8x8 button grid! is it plugged in??')
      exit(-1)    
    if portid >= 0:
      midithru.open_port(portid) 
      print("found out port for mf64-black.")
    else:
      print("couldnt find mf64-black output, how will my lights work??")

    # pick_colors()
    set_initial_colors()

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
    print("mf64 black:", evt, "transl:", data1+29)

    if status == constants.MIDI_NOTE_ON3:
        hardware.handle_button_press(data1)
    elif status == 130:
        should_activate = hardware.handle_button_release(data1)
        # maybe close out
        if should_activate >= 0:
          print("closing out..", should_activate, flush=True)
          rezzie.thru([146, should_activate, 127])

    # set on/off colors
    if status == constants.MIDI_NOTE_ON3:
        set_on_color(data1)
    elif status == constants.MIDI_NOTE_OFF3:
        set_off_color(data1)

    # forward everything to resolume
    rezzie.thru(evt)

def pick_colors():
    for x in range(36, 101):
        midithru.send_message([146, x, x+29])

def set_initial_colors():
    quads = config['quadrants']
    for layout in quads:
        for x in layout['buttons']:
           midithru.send_message([146, x, layout['off_color']])
           
def set_on_color(data1):
    print("finding on color..", flush=True)
    quads = config['quadrants']
    for layout in quads:
        if data1 in layout['buttons']:
           midithru.send_message([146, data1, layout['on_color']])
           print("found on color.", flush=True)
           return

def set_off_color(data1):
    quads = config['quadrants']
    for layout in quads:
        if data1 in layout['buttons']:
           midithru.send_message([146, data1, layout['off_color']])
           return

# better colors:
# blue: 114 or 90. press to 69 or 79
# orange: 96 or 126. press to 84
# purple: 82 or 95 or 107. press to 94
# green: 85 or 86. press to 87
