from vjmagic import constants
from vjmagic.interface import encoders

CONFIG = []

def load_config(myconfig):
  global CONFIG # @TODO why do I need this?
  CONFIG = myconfig


def check_for_category_change(event):
  (status, data1, data2) = event
  print("cat change:", event)
  # don't trust these... ex. resolume sends some crap.
  # if data2 == 0:
  #   return

  # we only want to look at the encoders we're tracking, ya know?
  # the 8x8 grid covers 36 to 99
  if data1 < 36 or data1 > 99:
    return

  for x in CONFIG:
    keys = x['keys']
    try:
      if keys.index(data1) >= 0:
        # print('checkin x:', x)
        if 'clips' in x:
        # try to find a thing in clips
          try:
              # print("lookin for 68:", x['clips'][0][0])
              clip = filter(lambda x: x[0] == data1, x['clips'])[0]
              if clip:
                  print(clip)
                  name = clip[1]
                  labels = clip[2]
                  # print(clip, name, labels)
                  # print('found specific clip:', name)
                  encoders.set_display_mode(x['mode'], labels, len(labels), name)
                  return
          except e:
              print(e)
              pass
        # else:
          # print('guess we didnt have clips.')
        # use the config's default stuff
        # print('nothing special found', x['mode'])
        encoders.set_display_mode(x['mode'], x['labels'], x['active'], '')
    except ValueError:
      pass
