
# buttonid: [active_layer, [dashboard knobs]]
# knobs are 0 to 7
# layers refers to the 1-indexed layer containing
# our effects and stuff
config = {
  'buttons': {
    36: [4, [0, 1]],
    37: [4, [2, 3]],
    38: [4, [4, 5]],
    39: [4, [6, 7]],
    40: [4, [0]],
    41: [4, [1]],
    42: [4, [2]],
    43: [4, [3]],
    44: [4, []],
    45: [4, []],
    46: [4, []],
    47: [4, []],
    48: [4, []],
    49: [4, []],
    50: [4, []],
    51: [4, []],

    52: [5, [0]],
    53: [5, [1, 2]],
    54: [5, [3]],
    55: [5, [4]],
    56: [5, [5]],
    57: [5, []],
    58: [5, [6]],
    59: [5, [0, 1]],

    60: [5, [7]],
    61: [5, []],
    62: [5, []],
    63: [5, [2]],
    64: [5, [3]],
    65: [5, []],
    66: [5, [4]], #type?
    67: [5, [5]], #type
  },
  # these map layers to which knobs are available.
  # knobs are labeled 0-15, right-to-left, top-to-bottom
  'layers': {
    3: [14, 15, 10, 11],
    4: [12, 13, 8, 9],
    5: [4, 5, 0, 1],
    6: [6, 7, 2, 3]
  }
}
