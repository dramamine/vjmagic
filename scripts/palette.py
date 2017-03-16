import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
push = available_ports.index("Ableton Push:Ableton Push MIDI 2 24:1")

if push >= 0:
    midiout.open_port(push)
else:
    midiout.open_virtual_port("My virtual output")


ci = 0
for note in range(36, 36+64):
  midiout.send_message([0x90, note, ci])
  ci = ci + 1

raw_input("Press Enter to continue...")

for note in range(36, 36+64):
  midiout.send_message([0x90, note, ci])
  ci = ci + 1

raw_input("Press Enter to continue...")

# cleanup
for note in range(36, 36+64):
  midiout.send_message([0x80, note, 0])

del midiout
