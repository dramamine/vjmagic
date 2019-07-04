from vjmagic.routers import twister
from vjmagic.interface import thereminmanager
from vjmagic.config.midifighter import config

buttons_pressed = []
# these are the buttons that inform twister or LED to do something;
# using this for SUPERKNOB / RAINBOW KNOB right now
button_whitelist = [
  39, 43, 47, 51,
  68, 69, 70, 71,
  72, 73, 74, 75,
  76, 77, 78, 79,
  80, 81, 82, 83
]

clips_pressed = []
clips_whitelist = [
  48, 49, 50,
  52, 53, 54,
  56, 57, 58,
  60, 61, 62,
  64, 65, 66
]

# @TODO remove
def load_config(mycfg):
  return

def handle_button_press(button):
  if (button in config['quadrants'][1]['buttons']):
    print('twister effect press')
    twister.handle_effect_press(not buttons_pressed)
    thereminmanager.press()
    buttons_pressed.append(button)

  if (button in clips_whitelist):
    clips_pressed.append(button)

# return "another button that you should press" to fighter64
def handle_button_release(button):
  if (button in config['quadrants'][1]['buttons']):
    buttons_pressed.remove(button)
    if not buttons_pressed:
      print('twister effect release')
      twister.handle_effect_release()
      thereminmanager.release()

  if (button in clips_whitelist):
    clips_pressed.remove(button)
    if not clips_pressed:
      # this is the 'kill button'
      return 44
    return clips_pressed[len(clips_pressed)-1]
  return -1



def f7(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]
