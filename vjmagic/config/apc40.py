from vjmagic.state import apc40
config = {
	'clips_banks': [
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
		0, 1,
		8, 9,
		16, 17,
		24, 25,
		32, 33
	],
	'clips_colors': [
		41, 61, 81, 101
	]
}
