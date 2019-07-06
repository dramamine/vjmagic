from vjmagic.interface import ledstrip, irsensor

# resolume instance
rezzie = None
# is this thing on?
on = False

# use these to adjust the arduino range
# NOTE: update this in ledstrip too
arduino_min = 100
arduino_max = 450
multiplier = (arduino_max - arduino_min) / 128

# store last resolume value - don't send if it's not an update
last_res_value = 0

def init(res):
    global rezzie
    rezzie = res
    irsensor.sense_things(handle_ir_value)
    # except:
    #     print("irsensor error")
    #     return None
    

# receive value from ir sensor
def handle_ir_value(value):
    global on, last_res_value
    if not on:
        return
    # tell ledstrip what we got
    ledstrip.cb(value)

    # convert value (250-600ish?? subject to change)
    # to the 0-127 range.
    converted = max(0, min(round((value-arduino_min)/multiplier), 127))
    
    if converted == last_res_value:
        return
    last_res_value = converted
    # tell resolume about our value
    # print('using value - converted', value, ' - ', converted)
    rezzie.thru([179, 15, converted])

# press one of the buttons we're listening for. note that
# this can get called even if its already on.
def press():
    global on
    if on:
        return
    print("toggling ears")
    irsensor.toggle_ears(True)
    on = True
    
# none of the buttons we're paying attention to are pressed.
def release():
    global on
    on = False
    print("toggling ears off")
    irsensor.toggle_ears(False)
    try:
        ledstrip.blackout()
    except:
        return None
