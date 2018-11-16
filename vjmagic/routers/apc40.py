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
active_clip = 0

# is the user holding SHIFT
shift_on = False

opacities = {}
opacity_disabled = {}

clip_layer_selected = 0
effects_layer_selected = 4

# which clip is active on each layer?
active_clip_by_layer = [-1, -1, -1, -1, -1, -1, -1, -1]

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
    # recolor_clips_bank(0)
    recolor_clips_leds(clip_layer_selected)
    recolor_effects_leds(effects_layer_selected)

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

    if check_for_layer_change(status, data1, data2) == True:
        print('changed layer')
        return

    if check_crossfader(status, data1, data2) == True:
        print('crossfaded')
        return

    # if check_for_bank_change(status, data1, data2) == False:
    #     return
    if modify_based_on_bank(status, data1, data2) == True:
        print('modified based on bank')
        return
    # if check_for_opacity(status, data1, data2) == False:
    #     return

    if check_shift(status, data1, data2) == True:
        return

    # forward everything to resolume
    rezzie.thru(evt)

# if a user presses the layer selector buttons
# then we use that to change which layer is touched by our main buttons
def check_for_layer_change(status, data1, data2):
    global clip_layer_selected, effects_layer_selected, active_clip_by_layer, shift_on
    if data1 != apc40.CLIP_STOP:
        return False
    clips_layers = config['clips_layers']
    effects_layers = config['effects_layers']
    idx = 0

    if shift_on:
        rezzie.thru([status+8, data1, data2])
        prinft('modified!!!!!', flush=True)
        return True

    for note in clips_layers:
        if status == note:
            clip_layer_selected = idx
            clip = active_clip_by_layer[idx]
            if clip >= 0:
                rezzie.thru([apc40.NOTE_ON_CH1 + clip_layer_selected, clip, 127])
                set_active(clip_layer_selected, clip)
            recolor_clips_leds(idx)
            return True
        idx = idx + 1
    # idx is should be 4 at this point
    for note in effects_layers:
        if status == note:
            effects_layer_selected = idx
            clip = active_clip_by_layer[idx]
            if clip >= 0:
                rezzie.thru([apc40.NOTE_ON_CH1 + clip_layer_selected, clip, 127])
                set_active(clip_layer_selected, clip)            
            recolor_effects_leds(idx)
            return True
        idx = idx + 1

def check_crossfader(status, data1, data2):
    if data1 == apc40.CROSSFADER:
        if data2 != 1:
            data1 = 67
        if status >= apc40.NOTE_OFF_CH1 and status <= apc40.NOTE_OFF_CH8:
            status = status + 16

        rezzie.thru([status, data1, 127])    
        return True
    return False

def check_shift(status, data1, data2):
    global shift_on
    if data1 == apc40.SHIFT and data2 == 127:
        if status == apc40.NOTE_ON_CH1:
            shift_on = True
        elif status == apc40.NOTE_OFF_CH1:
            shift_on = False
        print('shifted', flush=True)
        return True

def modify_based_on_bank(status, data1, data2):
    global active_clip, active_clip_by_layer
    if status != apc40.NOTE_ON_CH1 and status != apc40.NOTE_OFF_CH1:
        return False
    if data1 in config['clips_leds']:
        # just add "channels" for more room
        rezzie.thru([status + clip_layer_selected, data1, data2])
        set_active(clip_layer_selected, data1)
    elif data1 in config['effects_leds']:
        # hmm.. just add "channels" for more room?
        rezzie.thru([status + effects_layer_selected - 4, data1, data2])
        set_active(effects_layer_selected, data1)
    else:
        return False

    if status == apc40.NOTE_OFF_CH1:
        recolor_clips_led(data1, apc40.COLOR_GREEN_ENOUGH)
    return True
    
def set_active(layer, note):
    global active_clip_by_layer
    if layer < 4:
        layer_color = config['clips_colors'][layer]
    else:
        layer_color = config['effects_colors'][layer-4]
    
    recolor_clips_led(active_clip_by_layer[layer], layer_color)
    recolor_clips_led(note, apc40.COLOR_GREEN_ENOUGH)

    print("setting active clip by layer x to y:", layer, note);
    active_clip_by_layer[layer] = note


# num is 1-4 (which layer)
def recolor_clips_leds(layer):
    clips_leds = config['clips_leds']
    clips_colors = config['clips_colors']
    color = clips_colors[layer]
    for led in clips_leds:
         midithru.send_message([apc40.NOTE_ON_CH1, led, color])

# num is 5-8 (which layer)
def recolor_effects_leds(layer):
    print('recoloring layer:', layer)
    effects_leds = config['effects_leds']
    effects_colors = config['effects_colors']
    color = effects_colors[layer-4]
    for led in effects_leds:
        if led != active_clip_by_layer[layer]:
            midithru.send_message([apc40.NOTE_ON_CH1, led, color])

# recolor one LED. data1 is the value of the clip (40 different clip buttons)
# data should be in 'clips_leds'
def recolor_clips_led(led, color = 0):
    if led < 0:
        return False

    if color > 0:
        clip_color = color
    else:
        clip_color = config['clips_leds'].index(led)
    midithru.send_message([apc40.NOTE_ON_CH1, led, clip_color])



def init_lights():
    # this works fine for turning those 4 buttons on.
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.RECORD_BUTTON, 1])
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.SOLO_BUTTON, 1])
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.TRACK_SELECT, 1])
    # midithru.send_message([apc40.NOTE_ON_CH1, apc40.CROSSFADER, 2])

    # midithru.send_message([apc40.NOTE_ON_CH1, 0, 81])
    # midithru.send_message([apc40.NOTE_ON_CH1, 8, 82])
    # midithru.send_message([apc40.NOTE_ON_CH1, 16, 83])
    # midithru.send_message([apc40.NOTE_ON_CH1, 24, 84])

    return

