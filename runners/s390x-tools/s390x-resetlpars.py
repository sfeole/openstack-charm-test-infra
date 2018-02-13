#!/usr/bin/env python3
# This is the openstack deploy script for S390X and assumes ownership of 5 lpars
# LPAR {A..E} will be used and reset accordingly after the test is complete.
 
#Our Manual JuJu python bindings
from jujumanual import jujumanual

import os
import subprocess
import logging
import sys
import time

jujumanual = jujumanual("manual/127.0.0.1", "s390x_pike")
lvscript="scripts/lv.py"

# For Reference
#LPARA="ubuntu@10.13.3.10"
#LPARB="ubuntu@10.13.3.11"
#LPARC="ubuntu@10.13.3.12"
#LPARD="ubuntu@10.13.3.13"
#LPARE="ubuntu@10.13.3.14"
#LPAR5="ubuntu@10.13.3.5"
#LPAR6="ubuntu@10.13.3.6"
#LPAR7="ubuntu@10.13.3.7"
#LPAR8="ubuntu@10.13.3.8"
#LPAR9="ubuntu@10.13.3.9"

def resetlpars(lpar):
    ''' Create Snapshot on Lpar 
    '''

    try:
        logging.info("Reset the Lpars back to original snapshots")
        subprocess.run(["scp", lvscript, lpar+":/home/ubuntu/"], check=True)
        subprocess.run(["ssh", lpar, "/home/ubuntu/lv.py", "-r"], check=False)
    except subprocess.CalledProcessError as e:
        print(e)
        return False

def createsnapshot(lpar):
    ''' Create Snapshot on Lpar 
    '''

    try:
        logging.info("Reset the Lpars back to original snapshots")
        subprocess.run(["scp", lvscript, lpar+":/home/ubuntu/"], check=True)
        subprocess.run(["ssh", lpar, "/home/ubuntu/lv.py"], check=False)
    except subprocess.CalledProcessError as e:
        print(e)
        return False


def main():

#   Destroy the machines
    for i in range(5):
        i = str(i)
        jujumanual.remove_machine(i)

#   Destroy the controller
    jujumanual.destroy_controller()

#    #Sleeping 10 seconds to let things idle
    time.sleep(10)
    for i in range(5, 10):
        i = str(i)
        resetlpars("10.13.3." + i)
#    #sleep for 10 minutes, allow systems to reboot and merge their snapshots
    time.sleep(600)
##    #snapshot them again
    for i in range(5, 10):
        i = str(i)
        createsnapshot("10.13.3." + i)

if __name__ == "__main__":
    sys.exit(main())
