# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.state import hardware

rezzie = None
midiinput = None


# constructor
def init(skip = True):
    global midiinput
    # setup inputs
    midiinput = rtmidi.MidiIn()
    port = Router.find_port_index(midiinput, "midi fighter 64", skip)
    midiinput.open_port(port)
    midiinput.set_callback(handler)

def use(res):
    global rezzie
    rezzie = res

def thru(evt):
    print("thru called.", flush=True)
    rezzie.thru(evt)

# this handler's probably in every router
def handler(event, data=None):
    evt = event[0]
    (status, data1, data2) = evt
    print("mf64 black:", evt)

    if status == constants.MIDI_NOTE_ON3:
        hardware.handle_button_press(data1)
    elif status == 130:
        should_activate = hardware.handle_button_release(data1)
        # maybe close out
        if should_activate >= 0:
          print("closing out..", flush=True)
          rezzie.thru([146, should_activate, 127])

    # forward everything to resolume
    rezzie.thru(evt)
