# Example #2
# http://apps.sourceforge.net/trac/winappdbg/wiki/wiki/Debugging#Example_#2:_attaching_to_a_process_and_waiting_for_it_to_finish

from winappdbg import Debug

import sys

# Get the process ID from the command line
pid = int( sys.argv[1] )

# Instance a Debug object
debug = Debug()

# Attach to a running process
debug.attach( pid )

# Wait for the debugee to finish
debug.loop()
