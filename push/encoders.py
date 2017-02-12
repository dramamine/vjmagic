
STATUS = 176
ENCODERS = [71, 72, 73, 74, 75, 76, 77, 78, 79]

INCREMENT = 1
DECREMENT = 127

SENSITIVITY = 1

class Encoders:
    touched = [False] * 9
    values = [0] * 9
    ableton_out = None
    def __init(self):
        return
    def update_value(self, encoder, value):
        self.values[encoder] = value
    def register_listeners(self, listener):
        listener.add_listener([STATUS, None, None], self.handle_event)
    def load_output(self, ableton_out):
        self.ableton_out = ableton_out
    def handle_event(self, event):
        # print "Encoders got the event we wanted."
        (status, data1, data2) = event
        try:
            encoder = ENCODERS.index(data1)
        except ValueError:
            return None

        # splitting between increments and decrements
        if data2 < 64:
            self.values[encoder] = min(127, self.values[encoder] + (SENSITIVITY * data2) )
        else:
            self.values[encoder] = max(0, self.values[encoder] - (SENSITIVITY * (128 - data2) ) )

        self.update_display()

        # update display
    def update_display(self):
        val_strings = map(lambda x: str(x).center(8), self.values[:8])
        # annoying spacing
        outstr = ''
        ctr = 0
        for val_string in val_strings:
            outstr = outstr + val_string
            if ctr % 2 == 0:
                outstr = outstr + " "
            ctr = ctr + 1

        self.ableton_out.set_display_line(0, outstr)
