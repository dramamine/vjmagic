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

    # forward everything to resolume
    rezzie.thru(evt)

# if a user presses the layer selector buttons (none, 8 bars => 1/16)
# then we use that to change which layer is touched by our main buttons
def check_for_layer_change(status, data1, data2):
    global clip_layer_selected, effects_layer_selected
    if data1 != apc40.CLIP_STOP:
        return False
    clips_layers = config['clips_layers']
    effects_layers = config['effects_layers']
    idx = 0
    for note in clips_layers:
        if status == note:
            print('updating clip!')
            clip_layer_selected = idx
            recolor_clips_leds(idx)
            return True
        idx = idx + 1
    # idx is should be 4 at this point
    for note in effects_layers:
        if status == note:
            effects_layer_selected = idx
            recolor_effects_leds(idx)
            return True
        idx = idx + 1

# def check_for_bank_change(status, data1, data2):
#     global clips_bank
#     clips_banks = config['clips_banks']
#     idx = 0
#     for bank in clips_banks:
#         if status == bank[0] and data1 == bank[1]:
#             clips_bank = idx
#             print('ok! updating clip bank to:', idx)
#             recolor_clips_bank(idx)
#             recolor_clips_leds()
#             return True 
#         idx += 1
#     return True

def check_crossfader(status, data1, data2):
    if data1 == apc40.CROSSFADER:
        if data2 != 1:
            data1 = 67
        if status >= apc40.NOTE_OFF_CH1 and status <= apc40.NOTE_OFF_CH8:
            status = status + 16

        rezzie.thru([status, data1, 127])    
        return True
    return False

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

    # # update apc colors
    # if status == apc40.NOTE_ON_CH1:
    #     if data1 in config['clips_leds'] and data1 != active_clip:
    #         print('updating active clip from', active_clip, 'to', data1)
    #         recolor_clips_led(active_clip)
    #         active_clip = data1
    #         print('active clip is:', active_clip, dump=True)

    if status == apc40.NOTE_OFF_CH1:
        recolor_clips_led(data1, apc40.COLOR_GREEN_ENOUGH)
    return True
    

# def check_for_opacity(status, data1, data2):
#     global opacities, opacity_disabled, rezzie
#     # store opacities
#     if (status >= 176 and status <= 184) and data1 == apc40.TRACK_FADER:
#         # track_ids are 0-7
#         track_id = status - 176
#         if track_id in opacity_disabled and opacity_disabled[track_id]:
#             return False

#         opacities[track_id] = data2
#     if data1 == apc40.CLIP_STOP:
        
#         # if the button is pressed, set cc to 0.
#         # if the button is released, use the previous opacity
#         if (status >= 144 and status <= 152):
#             track_id = status - 144
#             opacity_disabled[track_id] = True

#             cc = 0
#             rezzie.thru([track_id + 176, apc40.TRACK_FADER, cc])

#             return False

#         if (status >= 128 and status <= 135):
#             track_id = status - 128
#             opacity_disabled[track_id] = False

#             cc = opacities[track_id]
#             rezzie.thru([track_id + 176, apc40.TRACK_FADER, cc])

#             return False

# def recolor_clips_bank(current_bank):
#     print("recoloring bank..", current_bank)
    # clips_banks = config['clips_banks']
    # clips_banks_off = config['clips_banks_off']

    idx = 0
    for message in clips_banks:
        if idx == current_bank:
            midithru.send_message(message)
        else:
            midithru.send_message(clips_banks_off[idx])
        idx += 1

def set_active(layer, note):
    global active_clip_by_layer
    if layer < 4:
        layer_color = config['clips_colors'][layer]
    else:
        layer_color = config['effects_colors'][layer-4]
    
    recolor_clips_led(active_clip_by_layer[layer], layer_color)
    recolor_clips_led(note, apc40.COLOR_GREEN_ENOUGH)

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
         midithru.send_message([apc40.NOTE_ON_CH1, led, color])

# recolor one LED. data1 is the value of the clip (40 different clip buttons)
# data should be in 'clips_leds'
def recolor_clips_led(led, color = 0):
    if led < 0:
        return False

    if color > 0:
        clip_color = color
    else:
        root_color = config['clips_colors'][clips_bank]
        clip_color = root_color + config['clips_leds'].index(led)
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

