from vjmagic import constants
config = [{
  'mode': 'BASIC',
  'active': 6,
  'quadrant': 2,
  'palette': 1,
  'killer': constants.BUTTON_DELETE,
  'kill_other_layer_on_select': 3,
  'labels': ['STR', 'MAG', 'INT', 'DEX', 'CON', 'LCK'],
  'keys': [
    68, 69, 70, 71,
    76, 77, 78, 79,
    84, 85, 86, 87,
    92, 93, 94, 95
  ],
  'clips': [
      [68, 'VHS and Back', ['Opac', 'Mode', 'Num', 'Dir', 'Speed', 'Static']],
      [69, 'Bzzzt (AB)', ['RGB', 'Zoom', 'Light', 'Frames']],
      [70, 'Boxy RGB (K)', ['Opac', 'Fun', 'Brite', 'Contra', 'Distort']],
      [76, 'Blow&Blur (A)', ['BlowX', 'BlowY', 'Blur', 'Str']],
      [77, 'Wowwave', ['Crest', 'Swell', 'Grid', 'Thick', 'Dworld']],
      [78, 'Demon Snap (WIP)', ['Opac', 'Link 2', 'Link 3', 'Link 4', 'Center', 'Link 6']],
      [95, '3D Glases Make This Beat Responsive', []]
    ]
}, {
  'mode': 'TOUCH',
  'active': 8,
  'quadrant': 3,
  'palette': 2,
  'killer': constants.BUTTON_UNDO,
  'kill_other_layer_on_select': 2,
  'keys': [
    72, 73, 74, 75,
    80, 81, 82, 83,
    88, 89, 90, 91,
    96, 97, 98, 99
  ],
  'clips': [
      [72, '1-900-TRYPTAFAX', ['Opac', 'Scale', 'DriveX', 'DriveY', 'Dvishn', 'Detail', 'Edge', 'Color']],
      [73, 'VHS Scrape', ['Direction', 'Motion', 'Speed']],
      [74, 'Big Wave', ['Opac', 'W', 'H', 'Rotate', 'Glitch', 'Str', 'Surface', 'Burn']],
      [75, 'Point Grid', ['Points', 'Reso']],
      [82, 'Luma Waves', []],
      [88, 'Spiral', ['none', 'Speed', 'TurnY', 'Wobble']],
      [89, 'Kapot', ['Link 1', 'Link 2']],
      [90, 'Recolour', []],
      [97, 'Classic Cube', ['Amount']],
      [98, 'Surface Refraction', []],
      [99, 'TIMELINE FUCKERY', ['Opac']],
    ]
}, {
  'mode': 'CLIPS',
  'active': 6,
  'quadrant': 0,
  'palette': 0,
  'killer': constants.BUTTON_QUANTIZE,
  'kill_other_layer_on_select': 1,
  'labels': ['intro', 'verse', 'chorus', 'bridge', 'break', 'outro'],
  'keys': [
    36, 37, 38, 39,
    44, 45, 46, 47,
    52, 53, 54, 55,
    60, 61, 62, 63
  ]
}, {
  'mode': 'CLIPS',
  'active': 6,
  'quadrant': 1,
  'palette': 0,
  'killer': constants.BUTTON_DOUBLE,
  'kill_other_layer_on_select': 0,
  'labels': ['intro', 'verse', 'chorus', 'bridge', 'break', 'outro'],
  'keys': [
    40, 41, 42, 43,
    48, 49, 50, 51,
    56, 57, 58, 59,
    64, 65, 66, 67
  ]
}]
