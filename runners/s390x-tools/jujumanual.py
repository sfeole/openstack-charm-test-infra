#!/usr/bin/env python3

import subprocess
import os

class jujumanual():
    """
    JuJu Manual Prov Class
    """

    def __init__(self, cloud, controllername, tags = '', bundle = ''):
        ''' Init with cloud/controller/tags, We conly require cloud and
            controller
        '''

        self.cloud = cloud
        self.controllername = controllername
        #I'm just brainstorming about tags, may not actually use them.
        self.tags = tags
        self.bundle = bundle

    def bootstrap_controller(self):
        ''' Bootstrap the JuJu Controller,
        Usage: self.bootstrap_controller()
        '''

        try:
            output = subprocess.run(["juju", "bootstrap", self.cloud,
                                      self.controllername, "--debug", "--constraints", 
                                     "tags=" + self.tags], check=True)
        except subprocess.CalledProcessError as e:
            return False

    def destroy_controller(self):
        ''' Destroy the controller & All Models
        '''

        try:
            output = subprocess.run(["juju", "destroy-controller", 
                                      self.controllername,
                                      "--destroy-all-models", "-y"],
                                     check=True)
        except subprocess.CalledProcessError as e:
            return False

    def add_machine(self, machineip):
        ''' Add a machine via the IP default user ubuntu is assumed
        Usage: self.machine(192.168.3.3)
        '''

        self.machineip = machineip
        
        try:
            output = subprocess.run(["juju", "add-machine", "ssh:ubuntu@" + self.machineip], check=True)
      
        except subprocess.CalledProcessError as e:
            return False

    def remove_machine(self, machine):
        ''' Remove a machine via the their numberical identifier, expects int not string.
        Usage: self.remove_machine(0)
        '''

        self.machine = machine
        
        try:
            output = subprocess.run(["juju", "remove-machine", self.machine, "--force" ], check=True)
      
        except subprocess.CalledProcessError as e:
            print(e)

    def deploybundle(self):
        ''' Deploy a bundle file
        Usage: self.deploy("path to bundle.yaml")
        '''

        try:
            output = subprocess.run(["juju", "deploy", self.bundle, "--map-machines=existing"], check=True)

        except subprocess.CalledProcessError as e:
            return False
