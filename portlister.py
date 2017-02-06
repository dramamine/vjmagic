import rtmidi

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()


for idx, val in enumerate(midiout.get_ports()):
    print "out port:", idx, val

for idx, val in enumerate(midiin.get_ports()):
    print "in port:", idx, val
