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
jujumanual = jujumanual("manual/10.245.162.222", "s390x_pike", bundle=BUNDLE)

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
    jujumanual.deploy()

if __name__ == "__main__":
    sys.exit(main())
