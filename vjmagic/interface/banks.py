from vjmagic import constants
from vjmagic.interface import outpututils, encodercontroller, graphics
from vjmagic.config.hypnodrome import config as hypno_new_config
from vjmagic.config.hypnotouch import config as hypnotouch_config
from time import sleep
current_config = constants.HYPNO_NEW

def color_bank_buttons():
  # light up our bank buttons
  for x in constants.BANK_BUTTONS:
    print("trying to color ", x)
    outpututils.note_sender([constants.STATUS_CH1, x, constants.BANK_COLOR_UNSELECTED])

def handle_presses(evt):
    global current_config
    (status, data1, data2) = evt
    print("handling bank press:", data1)
    if data1 == current_config:
        return

    if data1 in constants.BANK_BUTTONS:
        outpututils.clear_display()
        graphics.reset()
        # load up a config
        if data1 == constants.HYPNO_NEW:
            updated_config = hypno_new_config
            print("switching to hypno new")
            outpututils.set_display_line(1, "Switching to basic setup...")
            # encodercontroller.load_config(hypno_new_config)
            # print("hypno new config loaded")
            # for x in hypno_new_config:
            #     print("fixing graphics")
            #     graphics.reset()
            #     graphics.load_quadrant(**x)
            print("completed.")
        elif data1 == constants.HYPNO_ADV:
            updated_config = hypnotouch_config
            print("switching to hypno adv")
            outpututils.set_display_line(1, "Switching to ADVANCED setup... hope you know what you're doing!")
            # encodercontroller.load_config(hypnotouch_config)
            # print("hypno adv config loaded")
            # print("fixing graphics")
        else:
          print("Could not find that config!")
          return

        # assuming we were successful with finding config
        encodercontroller.load_config(updated_config)
        for x in updated_config:
            print("loading x:")
            graphics.load_quadrant(**x)

        print "setting current_config"
        current_config = data1
