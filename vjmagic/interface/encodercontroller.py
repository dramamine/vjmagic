from vjmagic import constants
from vjmagic.interface import encoders, outpututils

CONFIG = []

active_effect_clip = 70

def load_config(myconfig):
  print("new config loading")
  global CONFIG # @TODO why do I need this?
  CONFIG = myconfig

# return from clip to active effect
def handle_push_turns(event):
  global active_effect_clip
  if encoders.get_display_mode() == 'CLIPS' and active_effect_clip > 0:
    # sending to resolume
    mock_event = [constants.MIDI_NOTE_ON, active_effect_clip, 127]
    outpututils.thru(mock_event)
    check_for_category_change(mock_event)

def check_for_category_change(event):
  global CONFIG, active_effect_clip
  (status, data1, data2) = event
  # print("cat change:", event)
  # don't trust these... ex. resolume sends some crap.
  # if data2 == 0:
  #   return

  # we only want to look at the encoders we're tracking, ya know?
  # the 8x8 grid covers 36 to 99
  if data1 < 36 or data1 > 99:
    return

  # 'quadrants' tells us about which keys we care about.
  for x in CONFIG['quadrants']:
    keys = x['keys']
    try:
      if keys.index(data1) >= 0:
        if CONFIG['clips']:
          try:
              # check the 'clips' array for some mathing data.
              matching_clips = filter(lambda x: x[0] == data1, CONFIG['clips'])
              if matching_clips:
                  # gather data and fix the display & internal state
                  clip = matching_clips[0]
                  name = clip[1]
                  # included in config for effects,
                  # but for clips its [], so resolve to quad's labels
                  labels = clip[2] or x['labels']
                  audio_reactive = clip[3]

                  encoders.set_display_mode(x['mode'], labels, len(labels), name, audio_reactive)

                  # saving active clip
                  if x['mode'] != 'CLIPS':
                     active_effect_clip = data1

                  return
          except e:
              print(e)
              pass
        # else:
          # print('guess we didnt have clips.')
        # use the config's default stuff
        # print('nothing special found', x)
        encoders.set_display_mode(x['mode'], x['labels'], x['active'], '')
    except ValueError:
      pass
