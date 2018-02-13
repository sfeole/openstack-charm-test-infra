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

BUNDLE="./zopenstack/bundles/lpar/bundle.yaml"
jujumanual = jujumanual("manual/127.0.0.1", "s390x_pike", bundle=BUNDLE)

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


def main():
   #Check to see if we have a controller
    jujumanual.bootstrap_controller()
    for i in range(5, 10):
        i = str(i)
        jujumanual.add_machine("10.13.3." + i)
#
    jujumanual.deploybundle()

if __name__ == "__main__":
    sys.exit(main())
