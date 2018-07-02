from vjmagic.routers import fighter64
from vjmagic.routers import twister

buttons_pressed = []
button_whitelist = [
  39, 43, 47,
  68, 69, 70, 71,
  72, 73, 74, 75,
  76, 77, 78, 79
]

clips_pressed = []
clips_whitelist = [
  52, 53,
  56, 57,
  60, 61,
  64, 65
]

# @TODO remove
def load_config(mycfg):
  return

def handle_button_press(button):
  if (button in button_whitelist):
    twister.handle_effect_press(not buttons_pressed)
    buttons_pressed.append(button)

  if (button in clips_whitelist):
    clips_pressed.append(button)

# return "another button that you should press" to fighter64
def handle_button_release(button):
  if (button in button_whitelist):
    buttons_pressed.remove(button)
    if not buttons_pressed:
      twister.handle_effect_release()
  if (button in clips_whitelist):
    clips_pressed.remove(button)
    if not clips_pressed:
      # this is the 'kill button'
      return 67 
    return clips_pressed[len(clips_pressed)-1]
  return -1



def f7(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]