#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit
# games platform for kids using Raspberry Pi
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

import pygame
from pygame.locals import *

class Display:
    '''
    Screen graphics and other media are embedded in this class
    '''
    def __init__(self,CONF):

        self.CONF=CONF
        self.width=int(CONF["width"])
        self.height=int(CONF["height"])
        self.centerx=self.width/2
        self.centery=self.height/2
        
# Pygame modules initialization. Avoid general initialization because in some hardware you have no sound'
        pygame.font.init()
        pygame.display.init()
        pygame.mixer.init()
        
        if CONF["full_screen"] == "True":
            self.screen=pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode((self.width,self.height))

# Default font. Games can define their own ones
        self.default_font=pygame.font.Font(CONF["default_font"],int(CONF["default_font_size"])) 

# Default colors
        self.default_color=self.string_to_color(self.CONF["default_color"])
        self.default_background=self.string_to_color(self.CONF["default_background"])

# Change default mouse pointer
# "definition" is an array of strings containing a ascii map of an image made with "X" and "."
# Width and height must be multiply of 8
    def set_pointer(self, definition):
      size = (len(definition[0]), len(definition))
      print "Pointer size:", size
      data, mask = pygame.cursors.compile(definition, black='O',white='0',xor='o') 
      hotspot = (size[0]/2, size[1]/2)  # Set hotspot to centre
      pygame.mouse.set_cursor(size, hotspot, data, mask)

# Convert strings in real pygame colors
    def string_to_color(self, val):
        if len(val) == 3:
            rgb=map(int,val)
            return pygame.color.Color(rgb[0],rgb[1],rgb[2])
        else:
            return pygame.color.Color(val)


# Clear the screen
    def clean(self,color):
        self.screen.fill(color)
        pygame.display.flip()

# Fill the screen
    def fill(self,color):
        self.screen.fill(color)

# Dim to a color
    def fade(self, color=(0,0,0), speed=100):
        color_layer=pygame.Surface(self.screen.get_size())
        color_layer.fill(color)
        for n in range(128):
            color_layer.set_alpha(n*2)
            self.screen.blit(color_layer,(0,0))
            self.show()
            pygame.time.wait((100-speed))
        return

# Show changes in the screen
    def show(self):
        pygame.display.flip()


# Print an image and returns current screen content
    def print_image(self, image, x, y):
        current_content=pygame.Surface((image.get_width(),image.get_height()))
        current_content.blit(self.screen,(0,0),(x,y,image.get_width(),image.get_height()))
        self.screen.blit(image, (x,y))
        return current_content

# Print a text string, black and centered as default
    def print_text(self, text, font="", color="", x=-1, y=-1):
        
        if not font:
           font=self.default_font
        if not color:
            color=self.default_color
 
        rtext = font.render(text, 1, color)
        if x == -1:
            x=self.centerx - rtext.get_width() / 2
        if y == -1:
            y=self.centery - rtext.get_height() / 2
        self.screen.blit(rtext, (x,y))

# Print a text box (multiline), black on white and centered as default
    def print_textbox(self, text, font="", color="", background="", x=-1, y=-1):
        if not font:
            font=self.default_font
        if not color:
            color=self.default_color
        if not background:
            background=self.default_background

        margin=20
        font_height = font.get_height()
        lines=text.split("\n")

        surfaces = [font.render(line, True, tuple(color)) for line in lines]
        max_width = max([s.get_width() for s in surfaces])
        box = pygame.Surface((max_width+margin*2, len(lines)*font_height+margin*2), pygame.SRCALPHA)
        box.fill(background)

        for i in range(len(lines)):
           box.blit(surfaces[i], (margin,i*font_height+margin))

        if x == -1:
            x=self.centerx - box.get_width() / 2
        if y == -1:
            y=self.centery - box.get_height() / 2
        self.screen.blit(box, (x,y))
    

# Draw a box
    def print_box(self, w, h, x=-1,y=-1, color=(0,0,0)):
        if x == -1:
            x=self.centerx - w / 2
        if y == -1:
            y=self.centery - h / 2

        current_content=pygame.Surface((w,h))
        current_content.blit(self.screen,(0,0),(x,y,w,h))

        area=pygame.Rect((x,y),(w,h))
        self.screen.fill(color, area)
        return current_content

    
 

