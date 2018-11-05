# from push.listener import PushEventListener
# from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.state import hardware
from vjmagic.state import apc40
from vjmagic.config.skull import config
from math import floor

rezzie = None
midiinput = None
midithru = None
midiableton = None
abletoninput = None

clips_bank = 0
active_clip = 0

opacities = {}
opacity_disabled = {}

bank_button_left = False
bank_button_right = False
bank_button_offset = 0

# constructor
def init():
    global midiinput, midithru, midiableton, abletoninput
    # setup inputs
    midiinput = rtmidi.MidiIn()
    port = Router.find_port_index(midiinput, "apc40")
    midiinput.open_port(port)
    midiinput.set_callback(handler)

    abletoninput = rtmidi.MidiIn()
    port = Router.find_port_index(midiinput, "ableton out")
    if port >= 0:
        abletoninput.open_port(port)
        abletoninput.set_callback(handler)


    midithru = rtmidi.MidiOut()
    portid = Router.find_port_index(midithru, "apc40")
    if portid >= 0:
      midithru.open_port(portid) 
      print("found out port for apc40.")
    else:
      print("couldnt find apc40 output, how will my lights work??")

    midiableton = rtmidi.MidiOut()
    portid = Router.find_port_index(midithru, "ableton in")
    if portid >= 0:
      midiableton.open_port(portid)
    else:
      midiableton = None


    # init_lights()
    # recolor_clips_bank(0)
    recolor_clips_leds()

def use(res):
    global rezzie
    rezzie = res

def thru(evt):
    print("thru called.", flush=True)
    evt = event[0]
    (status, data1, data2) = evt
    rezzie.thru(evt)


def handler(event, data=None):
    evt = event[0]
    (status, data1, data2) = evt
    print("apc40", evt)

    # forward any events to Ableton. we want Ableton to have raw input from the
    # controller, so that the playback goes through the same logic 
    if midiableton:
        midiableton.send_message(evt)


    # bank buttons: [144, 60, 127], [144, 61, 127]
    if data1 in [60, 61]:
        handle_bank_buttons(status, data1)
        return

    # forward everything to resolume
    updated_data1 = data1 + bank_button_offset if (data1 < 40 and status == apc40.NOTE_ON_CH1 or status == apc40.NOTE_OFF_CH1) else data1
    print('updating clip:', updated_data1, flush=True)
    rezzie.thru([status, updated_data1, data2])

    if status == apc40.NOTE_ON_CH1 and data2 == 127:
        print('pressing clip', flush=True)
        handle_clip_pressed(data1)
    elif status == apc40.NOTE_OFF_CH1 and data2 == 0:
        handle_clip_released(data1)
    else:
        print('no rules found', flush=True)
    # if check_for_bank_change(status, data1, data2) == False:
    #     return
    # if modify_based_on_bank(status, data1, data2) == False:
    #     return
    # if check_for_opacity(status, data1, data2) == False:
    #     return

def handle_bank_buttons(status, data1):
    global bank_button_left, bank_button_right, bank_button_offset
    if data1 == apc40.BANK_BUTTON_LEFT:
        bank_button_left = (status == apc40.NOTE_ON_CH1)
    elif data1 == apc40.BANK_BUTTON_RIGHT:
        bank_button_right = (status == apc40.NOTE_ON_CH1)

    bank_button_offset = (40 * bank_button_left) + (80 * bank_button_right)
    print('bank_button_offset is now:', bank_button_offset, flush=True)


# clipid is 0 through 40ish
def handle_clip_pressed(clipid):
    layer = floor(clipid / 8)
    col = clipid % 8
    print(layer, col, flush=True)

    # scene launch buttons
    if layer == 10:
        return

    if bank_button_offset == 0:
        if col in [0, 1]:
            print('pressing a clip:', layer, col, flush=True)
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 0]) # set opacity to 0%
            rezzie.thru([apc40.FADERS_CH1, 48+layer, 48]) # set speed to 4x
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 66, 1]) # set direction to right
        elif col == 2:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 63]) # set opacity to 50%
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 49, 127]) # set layer opacity direction to pause
            rezzie.thru([apc40.FADERS_CH9+layer, 7, 127]) # set effect opacity to 100% (6th col. on apc40)
            rezzie.thru([apc40.NOTE_ON_CH9+layer, 49, 127]) # set effect direction to pause (6th col. on apc40)
        elif col >= 3:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 63]) # set opacity to 100%
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 49, 127]) # set direction to pause
    elif bank_button_offset == 40:
        if col == 0:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 127]) # set opacity to 100%
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 66, 1]) # set layer opacity direction to right
        elif col in [1, 6]:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 63]) # set opacity to 50%
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 49, 127]) # set layer opacity direction to pause
        elif col == 2:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 63]) # set opacity to 50%
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 49, 127]) # set layer opacity direction to pause
            rezzie.thru([apc40.FADERS_CH9+layer, 7, 127]) # set effect opacity to 100% (6th col. on apc40)
            rezzie.thru([apc40.NOTE_ON_CH9+layer, 49, 127]) # set effect direction to pause (6th col. on apc40)
        elif col == 5:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 127]) # set opacity to 100%
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 49, 127]) # set layer opacity direction to pause
        else:
            print('col 1 pauser?', flush=True)
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 127]) # set opacity to 100%
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 49, 127]) # set layer opacity direction to pause
        
            
def handle_clip_released(clipid):
    layer = floor(clipid / 8)
    col = clipid % 8

    # scene launch buttons
    if layer == 10:
        return

    if bank_button_offset == 0:
        if col == 0:
            print('releasing a clip:', flush=True)
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 63]) # set opacity to 50%
            rezzie.thru([apc40.FADERS_CH1, 48+layer, 48]) # set speed to 4x
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 50, 127]) # set direction to left
        elif col == 1:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 127]) # set opacity to 100%
            rezzie.thru([apc40.FADERS_CH1, 48+layer, 48]) # set speed to 4x
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 50, 127]) # set direction to left
        elif col == 2:
            rezzie.thru([apc40.NOTE_ON_CH9+layer, 50, 127]) # set effect direction to left (6th col. on apc40)
        elif col >= 3:
            rezzie.thru([apc40.NOTE_ON_CH2+layer, 49, 127]) # set direction to pause
    elif bank_button_offset == 40:
        if col == 0:
            rezzie.thru([apc40.NOTE_ON_CH9+layer, 50, 127]) # set effect direction to left (6th col. on apc40)
        elif col in [1, 5, 6]:
            rezzie.thru([apc40.FADERS_CH1+layer, 7, 0]) # set opacity to 0%
        elif col == 2:
            rezzie.thru([apc40.NOTE_ON_CH9+layer, 50, 127]) # set effect direction to left (6th col. on apc40)

    # recolor the clip
    recolor_clip_led(clipid)


def recolor_clips_leds():
    clips_colors = config['clips_colors']
    clip_color = clips_colors[clips_bank]
    for row in range(0,5):
        for col in range(0,9):
            midithru.send_message([apc40.NOTE_ON_CH1, col + 8*row, clips_colors[row]])

def recolor_clip_led(clipid):
    clips_colors = config['clips_colors']
    layer = floor(clipid / 8)
    midithru.send_message([apc40.NOTE_ON_CH1, clipid, clips_colors[layer]])

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

# def modify_based_on_bank(status, data1, data2):
#     global active_clip
#     if status != apc40.NOTE_ON_CH1 and status != apc40.NOTE_OFF_CH1:
#         return True

#     if data1 not in config['clips_leds']:
#         return True

#     # hmm.. just add "channels" for more room?
#     rezzie.thru([status + clips_bank, data1, data2])

#     # update apc colors
#     if status == apc40.NOTE_ON_CH1:
#         if data1 != active_clip:
#             print('updating active clip from', active_clip, 'to', data1)
#             recolor_clips_led(active_clip)
#             active_clip = data1
#             print('active clip is:', active_clip, dump=True)

#     if status == apc40.NOTE_OFF_CH1:
#         recolor_clips_led(data1, apc40.COLOR_GREEN_ENOUGH)
#     return False
    

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
#     clips_banks = config['clips_banks']
#     clips_banks_off = config['clips_banks_off']

#     idx = 0
#     for message in clips_banks:
#         if idx == current_bank:
#             midithru.send_message(message)
#         else:
#             midithru.send_message(clips_banks_off[idx])
#         idx += 1

# # recolor one LED. data1 is the value of the clip (40 different clip buttons)
# # data should be in 'clips_leds'
# def recolor_clips_led(led, color = 0):
#     if color > 0:
#         clip_color = color
#     else:
#         root_color = config['clips_colors'][clips_bank]
#         clip_color = root_color + config['clips_leds'].index(led)
#     midithru.send_message([apc40.NOTE_ON_CH1, led, clip_color])



# def init_lights():
#     # this works fine for turning those 4 buttons on.
#     # midithru.send_message([apc40.NOTE_ON_CH1, apc40.RECORD_BUTTON, 1])
#     # midithru.send_message([apc40.NOTE_ON_CH1, apc40.SOLO_BUTTON, 1])
#     # midithru.send_message([apc40.NOTE_ON_CH1, apc40.TRACK_SELECT, 1])
#     # midithru.send_message([apc40.NOTE_ON_CH1, apc40.CROSSFADER, 2])

#     midithru.send_message([apc40.NOTE_ON_CH1, 0, 81])
#     midithru.send_message([apc40.NOTE_ON_CH1, 8, 82])
#     midithru.send_message([apc40.NOTE_ON_CH1, 16, 83])
#     midithru.send_message([apc40.NOTE_ON_CH1, 24, 84])

#     return

