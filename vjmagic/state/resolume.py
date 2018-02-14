

active_layer = -1

buttons_pressed = set()
map_knobs_to_layers = []
button_map = {}

def load_map(mappy):
  global button_map
  button_map = mappy

def handle_button_press(button):
  buttons_pressed.add(button)
  # does that button have knobs?
  if (button in button_map):
    [layer, knobs] = button_map[button]
    print(layer)
    print(knobs)

def handle_button_release(button):
  buttons_pressed.remove(button)