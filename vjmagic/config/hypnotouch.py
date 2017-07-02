# Polyglitch: Line Width on dashboard knobs didn't work - always bounces back to 63.
# had to change it to Num Lines.
from vjmagic import constants
config = {
'name': 'hypnodrome_advanced',
'clips': [
[36, 'hexeosis_hx01', [], False] ,
[37, 'Mucky Secrets', [], False] ,
[38, "Reggie Watts - If You're Fcking, You're Fcking", [], False] ,
[39, '93~eskmo+urban', [], False] ,
[44, "Daphne Guinness 'Evening In Space' Directed by David LaChapelle", [], False] ,
[45, 'Kerli - Feral Hearts [mv]', [], False] ,
[46, 'Kamau Jambo [dance]', [], False] ,
[47, '189925156 - LUSH PUPPIES', [], False] ,
[52, 'AZEL PHARA - GREEN', [], False] ,
[53, 'Azaelia Banks - Chasing Time [mv]', [], False] ,
[54, '176703851 - CYCLE', [], False] ,
[55, 'Max Cooper - Waves', [], False] ,
[60, 'Fever the Ghost - Source [mv]', [], False] ,
[61, '187819565 - corollaria generation', [], False] ,
[62, 'Gravity [as]', [], False] ,
[63, 'Contre Temps [as]', [], False] ,
[40, 'Unleash Your Fingers 1', [], False] ,
[41, 'MAX COOPER SEED', [], False] ,
[42, 'Sony Bravia Bouncy Balls Full HD 1080p', [], False] ,
[43, '204849820 - PHEROMONE', [], False] ,
[48, 'Monument', [], False] ,
[49, '31~hooray4earth+fractal-zooming', [], False] ,
[50, '196269431 - Max Cooper - Order from Chaos - Official Video by Maxime Causeret', [], False] ,
[51, '8889015 - Jellyfish', [], False] ,
[56, 'Octopus Project', [], False] ,
[57, 'Moon', [], False] ,
[58, '180727317 - A E T H E R', [], False] ,
[59, '1 & 3 4', [], False] ,
[64, 'Longry', [], False] ,
[65, 'KLJM ESOL', [], False] ,
[66, 'ISOLATED', [], False] ,
[67, '8-bit Triangle Zoom', [], False] ,
[68, 'Fux Given', ['Rings', 'Parts', 'Fux', 'Lag', 'Twirl'], False] ,
[69, 'Pixelnoise', ['Noise', 'Reso', 'Satch', 'Fountain'], False] ,
[70, 'Triangulate ', ['Fractlity', 'Gentle'], True] ,
[71, 'Chance of Hail ', ['Slow Pour', 'Size', 'Twist', 'Blue ^', 'Red v'], True] ,
[76, 'Salvia', ['Bonkers', 'Timelines', 'Copies', 'Losing Focus', '', ''], False] ,
[77, 'Rotating Panels', ['Craze', 'Edge', 'Confuse'], False] ,
[78, 'Wavy Dots ', ['Color', 'Size', 'Count', 'Spread', 'Speed', 'Rotate', 'Zoom', ''], True] ,
[79, 'Busta Rhymes ', ['Invert', 'Focus', ''], True] ,
[84, 'Cyberscope ', ['Angles', 'Rotate', 'Cyber', 'C-Pass', ''], False] ,
[85, 'Flight', ['Tilt', 'Altitude', 'Height', 'Jags', 'Texture'], False] ,
[86, 'Go Negative ', ['Hue', 'Fisheye', 'Negs', 'Link 8'], True] ,
[87, 'Wowgrid ', ['Crest', 'Swell', 'Grid', 'Thick', ''], True] ,
[92, 'Spleigher ', ['Fun', 'Slay', 'Contra', 'Distort', 'Brite', 'Brite'], False] ,
[93, 'Tritunnel ', ['Tunnel', 'Speed', 'TurnX', 'TurnY', 'Fractality', '', '', ''], False] ,
[94, 'Stripwreck ', ['Yank', 'Tug', 'Strip', 'Wreck'], True] ,
[95, 'Ballmer ', ['Shape', '3D Reso', '2D Reso', 'Darkweb'], True] ,
[81, 'Lawl of Mirrors', ['FlipX', 'FlipY', 'Mirror', 'Mirror', 'Mirror', 'Mirror', 'Ocean', 'Motion'], False] ,
[82, 'VHS Scrape', ['Opac', 'Numb', 'Rotate', 'Moar', 'Runaway', 'Speed', 'Thick', 'Negate'], False] ,
[83, 'Big Wave', ['Opac', 'W', 'H', 'Rotate', 'Glitch', 'Str', 'Surface', 'Burn'], False] ,
[89, '1-900-TRYPTAFAX', ['Opac', 'Scale', 'DriveX', 'DriveY', 'Dvishn', 'Detail', 'Edge', 'Color'], False] ,
[90, 'Point Grid', ['Points', 'Reso', 'Worms', 'Trails', 'Tris', 'Tri Hard', 'TriStorm', 'Quads'], False] ,
[91, 'Recolour ', ['Mood', 'Pedal', 'Floor It', 'Sepial', 'Cellular', 'Micro', 'Scope', 'Antenna'], False] ,
[-1, 'Blow&Blur', ['BlowX', 'BlowY', 'Blur', 'Splits', 'Screens'], False] ,
[-1, 'Polyglitch', ['Color', 'Lines', 'Expand', 'Zoom', 'Fuzz'], False] ,
[-1, 'Point Grid ', ['Points', 'Reso', 'Worms', 'Trails', 'Quads', '', '', ''], False] ,
[-1, 'Posterize ', ['Posters', 'Satch'], True] ,
[-1, 'Bzzzt ', ['RGB', 'Zoom', 'Light', 'Frames'], True] ,
[-1, 'Horizontal ', ['Thick', 'Speed'], True] ,
[-1, 'Recolour ', ['Wiggity', 'Floor It', 'Cellular', 'Deckade', '', '', '', ''], True] ,
[-1, '', ['Color', 'Shape', 'Count', 'Edges', 'Rotate', 'Zoom', '', ''], True] ,
[-1, 'Audiosucker ', ['Suck', 'Poster'], True] ,
[-1, 'Oil Fire ', ['Distort', 'Spd', 'Deeds'], True] ,
[-1, 'Dubs ', ['Dubs'], True] ,
[-1, 'Happy Trails', ['Trails', 'Perma'], False] ,
[-1, 'Geequalizer', ['Reso', 'Extrude', 'Rotate', 'Zoom'], False] ,
],
'quadrants': [{
  'mode': 'BASIC',
  'active': 6,
  'quadrant': 2,
  'palette': 1,
  'killer': constants.BUTTON_DELETE,
  'kill_other_layer_on_select': -1,
  'keys': [
    68, 69, 70, 71,
    76, 77, 78, 79,
    84, 85, 86, 87,
    92, 93, 94, 95
  ],
}, {
  'mode': 'TOUCH',
  'active': 6,
  'quadrant': 3,
  'palette': 2,
  'killer': constants.BUTTON_UNDO,
  'kill_other_layer_on_select': -1,
  'keys': [
    81, 82, 83,
    89, 90, 91
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
