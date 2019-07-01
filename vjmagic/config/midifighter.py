config = {
  # clips vs masks: see fighter64white.py
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
      'buttons': [
        # 51, 80, 81, 82, 83, 
        55, 84, 85, 86, 87,
        59, 88, 89, 90, 91,
        63, 92, 93, 94, 95,
        67, 96, 97, 98, 99
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
        48, 49,
        50, 54, 58, 62, 66
      ]
    },
    {
      # green layer
      'off_color': 85,
      'on_color': 87,
      'buttons': [
        39, 68, 69, 70, 71,
        43, 72, 73, 74, 75,
        47, 76, 77, 78, 79
      ]
    }
  ]
}
