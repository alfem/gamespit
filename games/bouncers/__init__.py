#!/usr/bin/python
# -*- coding: utf8 -*-

# Bouncers

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

from Game import Game

class Menu(Game):

    def start(self):
      self.x=400
      self.y=10
      self.ix=1
      self.iy=1


    def loop(self):

      animals=("cat","cow","duck")
      which=0

      while True:
          self.x=self.x+self.ix
          self.y=self.y+self.iy
          if self.x > self.DISPLAY.width-150 or self.x < 0:
              self.ix=-self.ix

          if self.y > self.DISPLAY.height-150:
             self.iy=-self.iy

          self.iy=float(self.iy+0.01)

          self.fill()
          self.DISPLAY.print_image(self.IMAGES[animals[which]],self.x, self.y)
          self.DISPLAY.show()

          user_input=self.CONTROLLER.check_user_action()

          controller_type=user_input[0] 

          if controller_type == "K": #Keyboard
              key_name,key_modifiers=user_input[1:]

              if key_name:
                if key_name == "escape":
                    break
                which +=1
                if which == len(animals):
                    which = 0
          self.wait(6)


# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()

