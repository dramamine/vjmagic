from vjmagic import constants
from vjmagic.interface import outpututils, encodercontroller, graphics
from vjmagic.config.bankmap import bankmap

from time import sleep

active_bank = bankmap[0]

def color_bank_buttons():
  global active_bank
  # light up our bank buttons
  for x in constants.BANK_BUTTONS:

    if x == active_bank['key']:
        outpututils.note_sender([constants.STATUS_CH1, x, constants.BANK_COLOR_SELECTED])
    else:
        outpututils.note_sender([constants.STATUS_CH1, x, constants.BANK_COLOR_UNSELECTED])

def handle_presses(evt):
    global selected_bank, active_bank
    (status, data1, data2) = evt
    print("handling bank press:", data1)

    # presses only. this filters out un-presses
    if (data2 == 0):
      return

    if data1 not in constants.BANK_BUTTONS:
      return

    # ignore pressing the active bank
    print(active_bank['key'])
    if data1 == active_bank['key']:
        print("early exit")
        return

    new_bank = filter(lambda x: x['key'] == data1, bankmap)[0]
    print("loading bank:", new_bank)
    if not new_bank:
      print("Could not find that config!")
      return

    # clearing stuff
    outpututils.clear_display()
    graphics.reset()

    try:
        # assuming we were successful with finding config
        encodercontroller.load_config(new_bank['config'])
        for x in new_bank['config']['quadrant']:
            graphics.load_quadrant(**x)
    except Exception as e:
        raise e

    # save
    active_bank = new_bank
    color_bank_buttons()
