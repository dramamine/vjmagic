from vjmagic.state import apc40
config = {
	'clips_banks': [
		# these are messages that 
		[apc40.NOTE_ON_CH1, apc40.ACTIVATOR, 1],
		[apc40.NOTE_ON_CH1, apc40.CROSSFADER, 2],
		[apc40.NOTE_ON_CH1, apc40.SOLO_BUTTON, 1],
		[apc40.NOTE_ON_CH1, apc40.RECORD_BUTTON, 1],
	],
	'clips_banks_off': [
		[apc40.NOTE_ON_CH1, apc40.ACTIVATOR, 0],
		[apc40.NOTE_ON_CH1, apc40.CROSSFADER, 0],
		[apc40.NOTE_OFF_CH1, apc40.SOLO_BUTTON, 127],
		[apc40.NOTE_OFF_CH1, apc40.RECORD_BUTTON, 127],
	],
	'clips_leds': [
		0, 1, 2, 3,
		8, 9, 10, 11,
		16, 17, 18, 19,
		24, 25, 26, 27,
		32, 33, 34, 35
	],
	'clips_colors': [
		41, 61, 81, 99
	],

	'effects_leds': [
		4, 5, 6, 7,
		12, 13, 14, 15,
		20, 21, 22, 23,
		28, 29, 30, 31,
		36, 37, 38, 39
	],
	'effects_colors': [
		51, 71, 91, 111
	],

	'clips_layers': [
		apc40.NOTE_ON_CH1, apc40.NOTE_ON_CH2, apc40.NOTE_ON_CH3, apc40.NOTE_ON_CH4
	],
	'effects_layers': [
	   apc40.NOTE_ON_CH5, apc40.NOTE_ON_CH6, apc40.NOTE_ON_CH7, apc40.NOTE_ON_CH8
	]
}
