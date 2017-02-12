
class Router:
    self.midiout = None
    def __init(self, midiout):
        self.midiout = midiout
    def route(self, event, data=None):
        print event
        
