
STATUS_CH1 = 176
STATUS_CH2 = 177

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
        listener.add_listener([STATUS_CH1, None, None], self.handle_push_updates, True)
    def register_resolume_listener(self, listener):
        listener.add_listener([STATUS_CH2, None, None], self.handle_resolume_updates, True)
    def load_output(self, ableton_out):
        self.ableton_out = ableton_out
        self.update_display()
    def handle_push_updates(self, event):
        (status, data1, data2) = event
        try:
            encoder = ENCODERS.index(data1)
        except ValueError:
            return None

        # splitting between increments and decrements
        if data2 < 64:
            new_cc = min(127, self.values[encoder] + (SENSITIVITY * data2) )
        else:
            new_cc = max(0, self.values[encoder] - (SENSITIVITY * (128 - data2) ) )

        # relay the new value from ch1 to ch2
        self.ableton_out.thru([STATUS_CH2, data1, new_cc])

        # we were updating the display here...
        # but now lets try waiting for updates from resolume instead.
        # self.values[encoder] = new_cc
        # self.update_display()

    def handle_resolume_updates(self, event):
        (status, data1, data2) = event
        try:
            encoder = ENCODERS.index(data1)
        except ValueError:
            return None

        self.values[encoder] = data2
        self.update_display()

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
