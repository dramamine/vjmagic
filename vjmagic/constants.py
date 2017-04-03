MIDI_NOTE_ON = 0x90 # 144
COLOR_GREEN = 21

PRESS_USER_BUTTON = 0xB0 # 176

STATUS_CH1 = 0xB0 # 176
STATUS_CH2 = 0xB1 # 177
STATUS_CH3 = 0xB2 # 178
STATUS_CH4 = 0xB3 # 179

BUTTON_QUANTIZE = 116
BUTTON_DOUBLE = 117
BUTTON_DELETE = 118
BUTTON_UNDO = 119

LAYER_TOGGLE_BUTTONS = [BUTTON_QUANTIZE, BUTTON_DOUBLE, BUTTON_DELETE, BUTTON_UNDO]

ENCODERS = [71, 72, 73, 74, 75, 76, 77, 78, 79]

# those square buttons in the rightmost column
USER_BUTTONS_ROUTED_TO_CH3 = [
  110, 111, 112, 113, 114, 115,
  54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
  48, 49, 50, 51, 52, 53
]

CC_CHANGE = 0xB1 # 177
CC_EMU = 0xB2 # 178

GRAPHICS_KNOB = 14 # the leftmost knob

TEXT_SOLID_BARS = 5
TEXT_MID_BARS = 3
TEXT_NO_BARS = 6
TEXT_BLANK = 32
