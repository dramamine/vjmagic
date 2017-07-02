# Polyglitch: Line Width on dashboard knobs didn't work - always bounces back to 63.
# had to change it to Num Lines.
from vjmagic import constants
config = {
'clips': [
    [74, 'DUMMY EFFECT DO NOT USE', [], True] ,
    [75, 'DUMMY EFFECT DO NOT USE', [], True] ,
    [83, 'DUMMY EFFECT DO NOT USE', [], True] ,
    [72, 'Posterize (AB)', ['Posters', 'Satch'], True] ,
    [73, 'Bzzzt (AB)', ['RGB', 'Zoom', 'Light', 'Frames'], True] ,
    [80, 'Horizontal (A)', ['Thick', 'Speed'], True] ,
    [81, 'Recolour (AB)', ['Wiggity', 'Floor It', 'Cellular', 'Deckade'], True] ,
    [82, '(AR) Qualizer', ['Color', 'Shape', 'Count', 'Edges', 'Rotate', 'Zoom'], True] ,
    [88, 'Audiosucker (A)', ['Suck', 'Poster'], True] ,
    [89, 'Oil Fire (AB)', ['Distort', 'Spd', 'Deeds'], True] ,
    [90, '(AR) Wavy Dots', ['Color', 'Size', 'Count', 'Spread', 'Speed', 'Rotate', 'Zoom'], True] ,
    [91, 'Wowgrid (A)', ['Crest', 'Swell', 'Grid', 'Thick'], True] ,
    [96, 'Dubs (A)', ['Dubs'], True] ,
    [97, 'Triangulate (A)', ['Fractlty', 'Gentle'], True] ,
    [98, 'Ballmer (A)', ['Shape', '3D Reso', '2D Reso', 'Darkweb'], True] ,
    [68, 'DUMMY EFFECT DO NOT USE', [], False] ,
    [76, 'DUMMY EFFECT DO NOT USE', [], False] ,
    [69, 'Spleigher (B)', ['Fun', 'Slay', 'Contra', 'Distort', 'Brite', 'Brite'], False] ,
    [70, 'Blow&Blur', ['BlowX', 'BlowY', 'Blur', 'Splits', 'Screens'], False] ,
    [71, 'Flight', ['Tilt', 'Altitude', 'Height', 'Jags', 'Texture'], False] ,
    [77, 'Cyberscope (B)', ['Angles', 'Rotate', 'Cyber', 'C-Pass'], False] ,
    [78, 'Polyglitch', ['Color', 'Lines', 'Expand', 'Zoom', 'Fuzz'], False] ,
    [79, 'Chance of Hail (A?B)', ['Slow Pour', 'Size', 'Twist', 'Blue ^', 'Red v'], True] ,
    [84, 'Rotating Panels', ['Craze', 'Edge', 'Confuse'], False] ,
    [85, 'Point Grid (B)', ['Points', 'Reso', 'Worms', 'Trails', 'Quads'], False] ,
    [86, 'Pixelnoise', ['Noise', 'Reso', 'Satch', 'Fountain'], False] ,
    [87, 'Tritunnel (B)', ['Tunnel', 'Speed', 'TurnX', 'TurnY', 'Fractality'], False] ,
    [92, 'Happy Trails', ['Trails', 'Perma'], False] ,
    [93, 'Salvia', ['Bonkers', 'Timelines', 'Copies', 'Losing Focus'], False] ,
    [94, 'Fux Given', ['Rings', 'Parts', 'Fux', 'Lag', 'Twirl'], False] ,
    [95, 'Lawl of Mirrors', ['Ocean', 'Flipper', 'Mirror', 'Mirror', 'Mirror', 'Mirror'], False]
],
'quadrants': [{
  'mode': 'BASIC',
  'active': 6,
  'quadrant': 2,
  'palette': 1,
  'killer': constants.BUTTON_DELETE,
  'kill_other_layer_on_select': 1,
  'labels': ['STR', 'MAG', 'INT', 'DEX', 'CON', 'LCK'],
  'keys': [
    69, 70, 71,
    77, 78, 79,
    85, 86, 87,
    93, 94, 95
  ],
}, {
  'mode': 'BASIC',
  'active': 6,
  'quadrant': 3,
  'palette': 2,
  'killer': constants.BUTTON_UNDO,
  'kill_other_layer_on_select': 0,
  'keys': [
    72, 73, 74,
    80, 81, 82,
    88, 89, 90,
    96, 97, 98
  ],
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
}
