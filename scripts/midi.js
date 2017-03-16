var midi = require('midi');

// Set up a new output.
var output = new midi.output();

// Count the available output ports.
console.log( output.getPortCount() );

// Get the name of a specified output port.
console.log( output.getPortName(0) );

// Open the first available output port.
output.openPort(0);

// Send a MIDI message.
output.sendMessage([176,22,1]);

// Close the port when done.
output.closePort();
