# Spirent TestCenter Launcher Script
# Generated on Wed Dec 11 15:24:52 2019 by thinkpalm
# Framework ver. 4.94.6346.0000
#
# Comments: 
# 
#
# This launcher script invokes the following routines contained in the
# STC_Traffic_logic.py script. After sourcing the logic script,
# the logic flow is as follows:
#
# init - set the logging level and logging location (stdout).
#
# config - set up various test configuration parameters including:
#          - load the configuration into memory and set the STC port locations.
#            The port locations and the XML config file can be modified in this file.
#          - set the location for results files.
#            The location of the results files can be modified in this file.
#            This does not set the location of the log files. Set 
#            the STC_LOG_OUTPUT_DIRECTORY environment variable to choose 
#            a log file location.
#          - set up the sequencer.
#
# connect - perform the logical to physical port mapping, connect to the 
#           chassis' and reserve the ports.
#
# apply - write the configuration to the ports.
#
# run - execute the sequencer and obtain the test status from the 
#       Basic: Stop Command Sequence "Stopped Reason" value. If there
#       is no sequence defined, then the test state is returned: NONE,
#       PASSED or FAILED.
#
# cleanup - disconnect from the chassis (releases the ports) and reset 
#           the in memory configuration.
#
# return - return the test status obtained from the sequencer execution
#          to the caller.

import os
import sys
import STC_Traffic_logic as StcTest

def runTest():
    StcTest.init()
    StcTest.config( sys.path[0], [ '//192.168.0.15/2/2', '//192.168.0.15/2/3' ] )
    StcTest.connect()
    StcTest.apply()
    testState = StcTest.run()
    StcTest.cleanup()
    return testState

if __name__ == '__main__':
    if runTest() == 'FAILED':
        sys.exit(1)
    else:
        sys.exit(0)
