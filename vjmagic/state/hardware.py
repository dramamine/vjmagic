from vjmagic.routers import fighter64
from vjmagic.routers import twister

active_layer = -1

buttons_pressed = []
# this works better if we have some dummy data in here
active_knob_map = {
  3: [],
  4: [],
  5: [],
  6: []
}
button_map = {}
layers_to_knobs_map = {}

def load_config(mycfg):
  global button_map, layers_to_knobs_map
  button_map = mycfg['buttons']
  layers_to_knobs_map = mycfg['layers']

def handle_button_press(button):
  # buttons_pressed.add(button)
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

  # uniques, preserve order, first 4
  layer_map = f7(layer_map)[0:4]

  print("want to use layer map:", layer_map)
  print("knob map:", active_knob_map)
  old_count = len(active_knob_map[layer_to_reassess])
  new_count = len(layer_map)
  for i in range(1, 5):
    enc = layers_to_knobs_map[layer_to_reassess][i-1]
    if i > old_count and i <= new_count:
      twister.turn_on_light(enc)
    elif i <= old_count and i > new_count:
      twister.turn_off_light(enc)
  # if layer_to_reassess in active_knob_map and  != :
  #   print("probs need to turn on an encoder.")
  #   twister.turn_on_lights(layer, len(layer_map))

  active_knob_map[layer_to_reassess] = layer_map

def get_target_encoder(encoder):
  [layer, idx] = find_layer_position(encoder)

  # shouldn't happen
  if layer == -1:
    return -1

  if layer not in active_knob_map:
    return -1

  if idx not in active_knob_map[layer]:
    return -1

  dashboard = active_knob_map[layer][idx]
  cc = (layer - 3) * 8 + active
  print("targeting this cc:", cc, " from layer ", layer, " dashboard", dashboard)
  return cc


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
def find_layer_position(encoder):
  print(layers_to_knobs_map)
  for layer, encoders in layers_to_knobs_map.items():
    if encoder in encoders:
      return [layer, encoders.index(encoder)]
  return [-1, -1]

def f7(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]