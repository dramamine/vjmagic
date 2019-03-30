from vjmagic.interface import ledstrip, irsensor

# resolume instance
rezzie = None
# is this thing on?
on = False

last_res_value = 0

def init(res):
    global rezzie
    rezzie = res
    irsensor.sense_things(handle_ir_value)

# receive value from ir sensor
def handle_ir_value(value):
    global on, last_res_value
    if not on:
        # print('leaving early')
        return
    # tell ledstrip what we got
    ledstrip.cb(value)

    # convert value (100-600ish?? subject to change)
    # to the 0-127 range.
    converted = max(0, min(round(value/4), 127))
    
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
    irsensor.toggle_ears(True)
    on = True
    
# none of the buttons we're paying attention to are pressed.
def release():
    global on
    on = False
    irsensor.toggle_ears(False)
    ledstrip.blackout()
