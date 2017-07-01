from vjmagic import constants
config = [{
  'mode': 'BASIC',
  'active': 6,
  'quadrant': 2,
  'palette': 1,
  'killer': constants.BUTTON_DELETE,
  'kill_other_layer_on_select': 1,
  'labels': ['STR', 'MAG', 'INT', 'DEX', 'CON', 'LCK'],
  'keys': [
    68, 69, 70, 71,
    76, 77, 78, 79,
    84, 85, 86, 87,
    92, 93, 94, 95
  ],
  'clips': [
    [68, 'Salvia', ['Litespd', 'L-Split', 'Details', 'D-Zoom', 'Salvia', 'Folding'], False] ,
    [69, 'Spleigher', ['Opac', 'Fun', 'Brite', 'Contra', 'Distort'], False] ,
    [70, 'Wowgrid', ['Crest', 'Swell', 'Grid', 'Thick', 'Dworld'], False] ,
    [71, 'Oil Fire', ['Distort', 'Spd', 'DD'], False] ,
    [76, 'Triangulate', ['Opac', 'Detail', 'Tunnel', 'Speed', 'TurnX', 'TurnY'], False] ,
    [77, 'Blow&Blur', ['BlowX', 'BlowY', 'Blur', 'Splits', 'Screens'], False] ,
    [78, '3D Glasses', ['Opac', 'Mode', 'Trails', 'Rush', 'Suck'], False] ,
    [79, 'Bzzzt', ['RGB', 'Zoom', 'Light', 'Frames'], False] ,
    [84, 'Frac Fractal', ['Opac', 'Scale', 'Zoom', 'Imagine', 'Second', 'Scale'], False] ,
    [85, 'Stripe Sphere', ['Color', 'Color 2', 'Color 3', 'Style', 'Thick', 'Expand', 'Smooth', 'Zoom'], False] ,
    [86, 'Tako', ['Color', 'Size', 'Count', 'Curl', 'Expand', 'Disperse', 'Mirror', 'Link 8'], False] ,
    [87, 'Geequalizer', ['Reso', 'Extrude', 'Rotate', 'Zoom'], False] ,
    [92, 'Qualizer', ['Color', 'Shape', 'Count', 'Edges', 'Rotate', 'Zoom', 'Link 7', 'Link 8'], False] ,
    [93, '3Dizer', ['Color', 'Shape', 'Count', 'Style', 'Edges', 'Zoom', 'Link 7', 'Link 8'], False] ,
    [94, 'Wavy Dots', ['Color', 'Size', 'Count', 'Spread', 'Speed', 'Rotate', 'Zoom', 'Link 8'], False] ,
    [95, 'Polyglitch', ['Color', 'Size', 'Expand', 'Zoom'], False] ,
  ]
}, {
  'mode': 'TOUCH',
  'active': 8,
  'quadrant': 3,
  'palette': 2,
  'killer': constants.BUTTON_UNDO,
  'kill_other_layer_on_select': 0,
  'keys': [
    # 72, 73, 74, 75,
    81, 82, 83, # missing 80
    89, 90, 91, # missing 88
    # 96, 97, 98, 99
  ],
  'clips': [
    [81, 'Lawl of Mirrors', ['FlipX', 'FlipY', 'Mirror', 'Mirror', 'Mirror', 'Mirror', 'Ocean', 'Motion']] ,
    [82, 'VHS Scrape', ['Opac', 'Numb', 'Rotate', 'Moar', 'Runaway', 'Speed', 'Thick', 'Negate']] ,
    [83, 'Big Wave', ['Opac', 'W', 'H', 'Rotate', 'Glitch', 'Str', 'Surface', 'Burn']] ,
    [89, '1-900-TRYPTAFAX', ['Opac', 'Scale', 'DriveX', 'DriveY', 'Dvishn', 'Detail', 'Edge', 'Color']] ,
    [90, 'Point Grid', ['Points', 'Reso', 'Worms', 'Trails', 'Tris', 'Tri Hard', 'TriStorm', 'Quads']] ,
    [91, 'Recolour (B)', ['Mood', 'Pedal', 'Floor It', 'Sepial', 'Cellular', 'Micro', 'Scope', 'Antenna']] ,
    ]
}, {
  'mode': 'CLIPS',
  'active': 6,
  'quadrant': 0,
  'palette': 0,
  'killer': constants.BUTTON_QUANTIZE,
  'kill_other_layer_on_select': 3,
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
  'kill_other_layer_on_select': 2,
  'labels': ['intro', 'verse', 'chorus', 'bridge', 'break', 'outro'],
  'keys': [
    40, 41, 42, 43,
    48, 49, 50, 51,
    56, 57, 58, 59,
    64, 65, 66, 67
  ]
}]
