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
        self.numbers=int(self.CONF['GAME']['numbers'])
        self.minimun_rounds=int(self.CONF['GAME']['minimun_rounds'])
        self.maximun_rounds=int(self.CONF['GAME']['maximun_rounds'])
        return

    def loop(self):

        roulette_size=230
        PI=3.14

        while True:

          winner=random.randint(1,self.numbers)
          rounds=random.randint(self.minimun_rounds,self.maximun_rounds)

          degrees=int(360*rounds+winner*(360/self.numbers))

          for spin in range(degrees):
              self.fill()
          
              self.DISPLAY.print_image(self.IMAGES["arrow"],y=150)
 
              for d in range(self.numbers):
                  angle=d* 2*PI/self.numbers + spin*2*PI/360
                  x=self.DISPLAY.centerx+roulette_size*math.sin(angle) - 50
                  y=self.DISPLAY.centery+roulette_size*math.cos(angle) - 50
                  if d % 2:
                      self.DISPLAY.print_text(str(d+1), self.FONTS["Hominis100"],self.COLORS["text-odd"],x,y)
                  else:
                      self.DISPLAY.print_text(str(d+1), self.FONTS["Hominis100"],self.COLORS["text-even"],x,y)

              self.DISPLAY.show()

              delay=int(spin*10/degrees) # this makes roulette decelerate smoothly

              if self.CONTROLLER.check_user_action() == "K" and self.CONTROLLER.key_name == "escape": #quit game
                  break 

              self.wait(delay)


          if self.CONTROLLER.wait_for_user_action() == "K": #Keyboard
              if self.CONTROLLER.key_name == "escape": #quit game
                  break 


# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

