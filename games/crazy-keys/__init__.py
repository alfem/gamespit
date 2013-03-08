#!/usr/bin/python
# -*- coding: utf8 -*-

# Crazy Keys
#   My son loves hitting my keyboard. 
#   So I made this silly program to show random colors on screen. 
#   And maybe he will learn the letters! :-)

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 8/Mar/2013

import random

from Game import Game

class Menu(Game):

    def start(self):
        self.vowels='aeiou'


    def loop(self):

        while True:

          input_type=self.CONTROLLER.wait_for_user_action()


          if input_type == "K": #Keyboard
              char=self.CONTROLLER.key_name

              if char == "escape": #quit game
                  break 
              elif char in self.vowels: #you hit a vowel!
                  self.SOUNDS['vowel'].play()
              elif char.isdigit(): #you hit a number!
                  self.SOUNDS['number'].play()
              elif len(char) == 1: #you hit a consonant!
                  self.SOUNDS['consonant'].play()
              else: #you hit return, tab, or any other special key!
                  self.SOUNDS['other'].play()  
 
          bgcolor=(random.randint(0,255), random.randint(0,255),random.randint(0,255))
          charcolor=(random.randint(0,255), random.randint(0,255),random.randint(0,255))
          self.fill(bgcolor)
          self.DISPLAY.print_textbox(char, self.FONTS["embosst1100"],self.COLORS["text"], self.COLORS["text_background"])
          self.DISPLAY.show()


# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

