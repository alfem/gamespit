#!/usr/bin/python
# -*- coding: utf8 -*-

# telefam
# Super Simple Desktop for computer iliterated people in your family
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import pygame
from pygame.locals import *
import sys

class Control:
    '''
    User interaction class. Simple actions for up, down, left, right and ok can be activated with joystick, keyboard or any other device.
    '''
    def __init__(self,CONF):
        return

    def check_user_action(self):
            for event in pygame.event.get() :
# KEYBOARD
                if event.type == pygame.KEYDOWN :
                    keyname = pygame.key.name(event.key)
                    mods=pygame.key.get_mods()
                    if keyname == 'escape':
                        sys.exit(0)
                    if mods & KMOD_LSHIFT and keyname == 'escape':
                        sys.exit(0)
                    print keyname
                    return keyname,mods
            return 0,0
 
    def wait_for_user_action(self):
        while True:
            for event in pygame.event.get() :
# KEYBOARD
                if event.type == pygame.KEYDOWN :
                    keyname = pygame.key.name(event.key)
                    mods=pygame.key.get_mods()
                    if keyname == 'escape':
                        sys.exit(0)
                    if mods & KMOD_LSHIFT and keyname == 'escape':
                        sys.exit(0)
                    return keyname,mods


