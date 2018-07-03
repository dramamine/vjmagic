
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
  },
  # 86: red
  # 52: green
  # 1: blue
  'off_colors': [
    114, 63, 24, 0,
    63, 114, 64, 0,
    86, 48, 10, 0,
    86, 48, 10, 0
  ],
  'default_values': [
    0, 0, 0, 63,
    0, 63, 0, 63,
    0, 0, 0, 0,
    0, 0, 0, 0
  ],
  'quadrants': [
    {
      # blue layer
      'off_color': 114,
      'on_color': 69,
      'buttons': [36, 37, 40, 41]
    },
    {
      # orange layer
      'off_color': 126,
      'on_color': 84,
      'buttons': [39, 43, 47, 51,
        68, 69, 70, 71,
        72, 73, 74, 75,
        76, 77, 78, 79, 
        80, 81, 82, 83
      ]
    },
    {
      # purple layer
      'off_color': 82,
      'on_color': 94,
      'buttons': [
        52, 53,
        56, 57,
        60, 61,
        64, 65,
        48, 49
      ]
    },
    {
      # green layer
      'off_color': 85,
      'on_color': 87,
      'buttons': [
        59, 63, 67,
        88, 89, 90, 91,
        92, 93, 94, 95,
        96, 97, 98, 99
      ]
    }
  ]
}
