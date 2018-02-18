from vjmagic.routers import fighter64

active_layer = -1

buttons_pressed = []
active_knob_map = []
map_knobs_to_layers = []
button_map = {}

def load_map(mappy):
  global button_map
  button_map = mappy

def handle_button_press(button):
  buttons_pressed.add(button)
  # does that button have knobs?
  if (button in button_map):
    buttons_pressed.append(button)
    [layer, knobs] = button_map[button]
    print(layer)
    print(knobs)
    reassess_layer(layer)

def handle_button_release(button):
  buttons_pressed.remove(button)
  [layer, knobs] = button_map[button]
  reassess_layer(layer)

def reassess_layer(layer_to_reassess):
  layer_map = []
  for button in buttons_pressed:
    [layer, knobs] = button_map[button]
    if layer_to_reassess == layer:
      layer_map.extend(knobs)
  layer_map = layer_map[0:4]

  if len(active_knob_map[layer]) != len(layer_map):
    fighter64.turn_on_lights(layer, len(layer_map))

  active_knob_map[layer] = layer_map

# def sync_knobs():
#   # calculate knob map
#   knob_map = []
#   for button in buttons_pressed:
#     [layer, knobs] = button_map[button]
#     if (knob_map[layer]):
#       knob_map[layer].extend(knobs)
#     else:
#       knob_map[layer] = knobs

#   # possible active layers
#   for layer in range(3, 6):
#     if active_knobs[layer] && !knob_map[layer]:
