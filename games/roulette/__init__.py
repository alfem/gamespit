#!/usr/bin/python
# -*- coding: utf8 -*-

# Roulette
#   A basic roulette you can use as a dice

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 8/Mar/2013

import random
import math

from Game import Game

class Menu(Game):

    def start(self):
        return

    def loop(self):

        roulette_size=230
        PI=3.14
        digits=6

        while True:

          winner=random.randint(1,digits)
          rounds=random.randint(3,6)

          degrees=360*rounds+winner*(360/digits)

          for spin in range(degrees):
              self.fill()
 
              for d in range(digits):
                  angle=d* 2*PI/digits + spin*2*PI/360
                  x=self.DISPLAY.centerx+roulette_size*math.sin(angle) - 50
                  y=self.DISPLAY.centery+roulette_size*math.cos(angle) - 50
                  if d % 2:
                      self.DISPLAY.print_text(str(d+1), self.FONTS["Hominis100"],self.COLORS["text-odd"],x,y)
                  else:
                      self.DISPLAY.print_text(str(d+1), self.FONTS["Hominis100"],self.COLORS["text-even"],x,y)

              self.DISPLAY.show()

              delay=spin*10/degrees # this makes roulette decelerate smoothly
              self.wait(delay)


          if self.CONTROLLER.wait_for_user_action() == "K": #Keyboard
              if self.CONTROLLER.key_name == "escape": #quit game
                  break 


# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

