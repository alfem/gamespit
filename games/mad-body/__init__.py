#!/usr/bin/python
# -*- coding: utf8 -*-

# Mad Body
#   Swap heads and bodies from a funny catalog

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 8/Mar/2013

import random

from Game import Game

class Menu(Game):

    def start(self):
        self.heads=0
        self.bodies=0
        self.legs=0
        for name in self.IMAGES:
            if name[0:4] == 'head':
                self.heads += 1
            elif name[0:4] == 'body':
                self.bodies += 1
            elif name[0:4] == 'legs':
                self.legs += 1
        return

    def loop(self):

        while True:

          head=random.randint(0,self.heads-1)
          body=random.randint(0,self.bodies-1)
          legs=random.randint(0,self.legs-1)

          self.fill()
 
          self.DISPLAY.print_image(self.IMAGES["head"+str(head)],y=50)
          self.DISPLAY.print_image(self.IMAGES["body"+str(body)],y=200)
          self.DISPLAY.print_image(self.IMAGES["legs"+str(legs)],y=360)

          self.DISPLAY.show()

          if self.CONTROLLER.wait_for_user_action() == "K": #Keyboard
              if self.CONTROLLER.key_name == "escape": #quit game
                  break 


# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

