#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit
# games platform for kids using Raspberry Pi
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import pygame
from pygame.locals import *
import sys

class Control:
    '''
    User interaction class. 
    '''
    def __init__(self,CONF):
        self.reset()
        return

    def reset(self):
        self.key_name=""
        self.key_modifiers=""
        self.mouse_position=(0,0)
        self.mouse_button=""
        return

# Check keyboard or mouse clicks and return without waiting
    def check_user_action(self):
        self.reset()
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN: # KEYBOARD
                self.key_name = pygame.key.name(event.key)
                self.key_mods=pygame.key.get_mods()
                if self.key_mods & KMOD_LSHIFT and self.key_name == 'escape':
                    sys.exit(0)
                return "K"
            if event.type == pygame.MOUSEBUTTONDOWN: # MOUSE
                self.mouse_position=event.pos
                self.mouse_button=event.button 
                return "M"
        return "N"
 
# Stop until user press a key or a mouse button
    def wait_for_user_action(self):
        self.reset()
        while True:
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN: # KEYBOARD
                    self.key_name = pygame.key.name(event.key)
                    self.key_mods=pygame.key.get_mods()
                    if self.key_mods & KMOD_LSHIFT and self.key_name == 'escape':
                        sys.exit(0)
                    return "K"

                if event.type == pygame.MOUSEBUTTONDOWN: # MOUSE
                    self.mouse_position=event.pos
                    self.mouse_button=event.button 
                    return "M"
        return "N" 
