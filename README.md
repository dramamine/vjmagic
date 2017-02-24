## MIDI TOOLS

Intended audience: me

## How To Install
pip install -r requirements.txt

## How To Test
python testrunner.py

## Main File
python push.py

## What's your MIDI setup?
Use loopMIDI to define the virtual ports you need.

"ableton push (main buttons) (out)" => python
"ableton push (other buttons) (out)" => python
"resolume out" => python

virtual port "python out":
python => "midiout2 (ableton push)"
